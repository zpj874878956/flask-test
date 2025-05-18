import os
import ftplib
from flask import current_app
import uuid

class FTPClient:
    def __init__(self):
        self.host = current_app.config['FTP_HOST']
        self.port = current_app.config['FTP_PORT']
        self.username = current_app.config['FTP_USERNAME']
        self.password = current_app.config['FTP_PASSWORD']
        self.directory = current_app.config['FTP_DIRECTORY']
        self.ftp = None
    
    def connect(self):
        """连接到 FTP 服务器"""
        try:
            self.ftp = ftplib.FTP()
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            
            # 尝试切换到指定目录，如果不存在则创建
            try:
                self.ftp.cwd(self.directory)
            except ftplib.error_perm:
                # 目录不存在，创建目录
                self._create_directory_tree(self.directory)
                self.ftp.cwd(self.directory)
                
            return True
        except Exception as e:
            current_app.logger.error(f"FTP 连接错误: {str(e)}")
            return False
    
    def _create_directory_tree(self, directory):
        """递归创建目录树"""
        if directory == '/':
            return
        
        parent = os.path.dirname(directory)
        if parent and parent != '/':
            try:
                self.ftp.cwd(parent)
            except ftplib.error_perm:
                self._create_directory_tree(parent)
                self.ftp.cwd(parent)
        
        try:
            self.ftp.mkd(os.path.basename(directory))
        except ftplib.error_perm:
            pass  # 目录可能已存在
    
    def disconnect(self):
        """断开 FTP 连接"""
        if self.ftp:
            self.ftp.quit()
            self.ftp = None
    
    def upload_file(self, file_data, original_filename, version_id):
        """上传文件到 FTP 服务器"""
        if not self.connect():
            return None
        
        try:
            # 创建版本目录
            version_dir = f"version_{version_id}"
            try:
                self.ftp.cwd(version_dir)
            except ftplib.error_perm:
                self.ftp.mkd(version_dir)
                self.ftp.cwd(version_dir)
            
            # 生成唯一文件名
            file_ext = os.path.splitext(original_filename)[1]
            unique_filename = f"{uuid.uuid4().hex}{file_ext}"
            
            # 上传文件
            self.ftp.storbinary(f'STOR {unique_filename}', file_data)
            
            # 返回文件路径
            file_path = f"{self.directory}/{version_dir}/{unique_filename}"
            return {
                'filename': unique_filename,
                'original_filename': original_filename,
                'file_path': file_path
            }
        except Exception as e:
            current_app.logger.error(f"文件上传错误: {str(e)}")
            return None
        finally:
            self.disconnect()
    
    def download_file(self, file_path):
        """从 FTP 服务器下载文件"""
        if not self.connect():
            return None
        
        try:
            # 提取目录和文件名
            directory = os.path.dirname(file_path.replace(self.directory, '', 1))
            filename = os.path.basename(file_path)
            
            # 切换到文件所在目录
            if directory:
                self.ftp.cwd(directory)
            
            # 创建内存文件对象
            from io import BytesIO
            file_data = BytesIO()
            
            # 下载文件
            self.ftp.retrbinary(f'RETR {filename}', file_data.write)
            
            # 将文件指针移到开始位置
            file_data.seek(0)
            return file_data
        except Exception as e:
            current_app.logger.error(f"文件下载错误: {str(e)}")
            return None
        finally:
            self.disconnect()