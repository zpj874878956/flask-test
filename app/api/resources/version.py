from flask import request, current_app
from flask.views import MethodView
from app.services.version_service import VersionService
from app.services.product_service import ProductService

class VersionListResource(MethodView):
    def get(self):
        """获取版本列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        status = request.args.get('status')
        product_id = request.args.get('product_id', type=int)
        
        if product_id:
            pagination = VersionService.get_versions_by_product(
                product_id=product_id,
                page=page,
                per_page=per_page,
                status=status
            )
        else:
            return {'success': False, 'message': '必须提供产品ID'}, 400
        
        versions = pagination.items
        
        return {
            'success': True,
            'data': {
                'versions': [version.to_dict() for version in versions],
                'total': pagination.total,
                'pages': pagination.pages,
                'current_page': pagination.page
            }
        }
    
    def post(self):
        """创建新版本"""
        data = request.get_json()
        
        if not data:
            return {'success': False, 'message': '无效的请求数据'}, 400
        
        product_id = data.get('product_id')
        version_number = data.get('version_number')
        description = data.get('description', '')
        release_notes = data.get('release_notes', '')
        author_id = data.get('author_id')
        status = data.get('status', 'draft')
        
        if not product_id or not version_number or not author_id:
            return {'success': False, 'message': '产品ID、版本号和作者ID不能为空'}, 400
        
        # 检查产品是否存在
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return {'success': False, 'message': '指定的产品不存在'}, 404
        
        version = VersionService.create_version(
            product_id=product_id,
            version_number=version_number,
            description=description,
            release_notes=release_notes,
            author_id=author_id,
            status=status
        )
        
        return {'success': True, 'data': version.to_dict()}, 201

class VersionResource(MethodView):
    def get(self, version_id):
        """获取版本详情"""
        version = VersionService.get_version_by_id(version_id)
        
        if not version:
            return {'success': False, 'message': '版本不存在'}, 404
        
        return {'success': True, 'data': version.to_dict()}
    
    def put(self, version_id):
        """更新版本信息"""
        version = VersionService.get_version_by_id(version_id)
        
        if not version:
            return {'success': False, 'message': '版本不存在'}, 404
        
        data = request.get_json()
        
        if not data:
            return {'success': False, 'message': '无效的请求数据'}, 400
        
        # 不允许更改产品ID和作者ID
        if 'product_id' in data:
            del data['product_id']
        if 'author_id' in data:
            del data['author_id']
        
        updated_version = VersionService.update_version(
            version_id=version_id,
            **data
        )
        
        return {'success': True, 'data': updated_version.to_dict()}
    
    def delete(self, version_id):
        """删除版本"""
        result = VersionService.delete_version(version_id)
        
        if not result:
            return {'success': False, 'message': '版本不存在或无法删除'}, 400
        
        return {'success': True, 'message': '版本已成功删除'}, 200

class VersionHistoryResource(MethodView):
    def get(self, product_id):
        """获取产品的版本历史"""
        # 检查产品是否存在
        product = ProductService.get_product_by_id(product_id)
        if not product:
            return {'success': False, 'message': '指定的产品不存在'}, 404
        
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        status = request.args.get('status')
        
        pagination = VersionService.get_versions_by_product(
            product_id=product_id,
            page=page,
            per_page=per_page,
            status=status
        )
        
        versions = pagination.items
        
        return {
            'success': True,
            'data': {
                'product': product.to_dict(),
                'versions': [version.to_dict() for version in versions],
                'total': pagination.total,
                'pages': pagination.pages,
                'current_page': pagination.page
            }
        }