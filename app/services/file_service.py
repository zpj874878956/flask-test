from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        db.session.add(file)
        db.session.commit()
        return file
    
    @staticmethod
    def get_file_by_id(file_id):
        """根据 ID 获取文件"""
        return File.query.get(file_id)
    
    @staticmethod
    def get_files_by_version(version_id):
        """获取指定版本的所有文件"""
        return File.query.filter_by(version_id=version_id).all()
    
    @staticmethod
    def download_file(file_id):
        """下载文件"""
        file = File.query.get(file_id)
        if not file:
            return None
        
        ftp_client = FTPClient()
        file_data = ftp_client.download_file(file.file_path)
        
        if not file_data:
            return None
        
        return {
            'file_data': file_data,
            'filename': file.original_filename,
            'file_type': file.file_type
        }
    
    @staticmethod
    def delete_file(file_id):
        """删除文件"""
        file = File.query.get(file_id)
        if not file:
            return False
        
        # 这里可以添加从 FTP 服务器删除文件的逻辑
        # 但为了保留历史记录，通常不会物理删除文件
        
        db.session.delete(file)
        db.session.commit()
        return True
from app.extensions import db
from app.models.file import File
from app.utils.ftp_client import FTPClient
import os

class FileService:
    @staticmethod
    def upload_file(file_data, original_filename, version_id, uploader_id):
        """上传文件"""
        # 获取文件类型和大小
        file_type = os.path.splitext(original_filename)[1][1:].lower()
        file_size = len(file_data.read())
        file_data.seek(0)  # 重置文件指针
        
        # 上传到 FTP 服务器
        ftp_client = FTPClient()
        result = ftp_client.upload_file(file_data, original_filename, version_id)
        
        if not result:
            return None
        
        # 创建文件记录
        file = File(
            filename=result['filename'],
            original_filename=result['original_filename'],
            file_path=result['file_path'],
            file_size=file_size,
            file_type=file_type,
            version_id=version)