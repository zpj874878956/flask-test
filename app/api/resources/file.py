from flask import request, jsonify, send_file
from flask.views import MethodView
from app.services.file_service import FileService
from app.models.version import Version
from app.extensions import db
import io

class FileUploadResource(MethodView):
    def post(self):
        """上传文件"""
        # 检查是否有文件
        if 'file' not in request.files:
            return jsonify({'error': '没有文件'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 获取版本 ID 和上传者 ID
        version_id = request.form.get('version_id')
        uploader_id = request.form.get('uploader_id')
        
        if not version_id or not uploader_id:
            return jsonify({'error': '缺少必要参数: version_id 或 uploader_id'}), 400
        
        # 检查版本是否存在
        version = Version.query.get(version_id)
        if not version:
            return jsonify({'error': f'版本ID {version_id} 不存在，请先创建版本'}), 404
        
        # 上传文件
        file_record = FileService.upload_file(
            file_data=file,
            original_filename=file.filename,
            version_id=version_id,
            uploader_id=uploader_id
        )
        
        if not file_record:
            return jsonify({'error': '文件上传失败'}), 500
        
        return jsonify(file_record.to_dict()), 201

class FileDownloadResource(MethodView):
    def get(self, file_id):
        """下载文件"""
        result = FileService.download_file(file_id)
        
        if not result:
            return jsonify({'error': '文件不存在或下载失败'}), 404
        
        return send_file(
            io.BytesIO(result['file_data'].read()),
            mimetype=f'application/{result["file_type"]}',
            as_attachment=True,
            download_name=result['filename']
        )

class FileListResource(MethodView):
    def get(self):
        """获取版本的所有文件"""
        version_id = request.args.get('version_id')
        
        if not version_id:
            return jsonify({'error': '缺少必要参数: version_id'}), 400
        
        files = FileService.get_files_by_version(version_id)
        return jsonify([file.to_dict() for file in files])