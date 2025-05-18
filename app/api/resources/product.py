from flask import request, current_app
from flask.views import MethodView
from app.services.product_service import ProductService

class ProductListResource(MethodView):
    def get(self):
        """获取产品列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        status = request.args.get('status')
        
        pagination = ProductService.get_all_products(page=page, per_page=per_page, status=status)
        products = pagination.items
        
        return {
            'success': True,
            'data': {
                'products': [product.to_dict() for product in products],
                'total': pagination.total,
                'pages': pagination.pages,
                'current_page': pagination.page
            }
        }
    
    def post(self):
        """创建新产品"""
        data = request.get_json()
        
        if not data:
            return {'success': False, 'message': '无效的请求数据'}, 400
        
        name = data.get('name')
        description = data.get('description', '')
        code = data.get('code')
        status = data.get('status', 'active')
        
        if not name or not code:
            return {'success': False, 'message': '产品名称和代码不能为空'}, 400
        
        product = ProductService.create_product(
            name=name,
            description=description,
            code=code,
            status=status
        )
        
        return {'success': True, 'data': product.to_dict()}, 201

class ProductResource(MethodView):
    def get(self, product_id):
        """获取产品详情"""
        product = ProductService.get_product_by_id(product_id)
        
        if not product:
            return {'success': False, 'message': '产品不存在'}, 404
        
        return {'success': True, 'data': product.to_dict()}
    
    def put(self, product_id):
        """更新产品信息"""
        product = ProductService.get_product_by_id(product_id)
        
        if not product:
            return {'success': False, 'message': '产品不存在'}, 404
        
        data = request.get_json()
        
        if not data:
            return {'success': False, 'message': '无效的请求数据'}, 400
        
        updated_product = ProductService.update_product(
            product_id=product_id,
            name=data.get('name', product.name),
            description=data.get('description', product.description),
            code=data.get('code', product.code),
            status=data.get('status', product.status)
        )
        
        return {'success': True, 'data': updated_product.to_dict()}
    
    def delete(self, product_id):
        """删除产品"""
        result = ProductService.delete_product(product_id)
        
        if not result:
            return {'success': False, 'message': '产品不存在或无法删除'}, 400
        
        return {'success': True, 'message': '产品已成功删除'}, 200