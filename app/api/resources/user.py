from flask import request, jsonify
from flask.views import MethodView
from app.services.user_service import UserService

class UserResource(MethodView):
    def get(self, user_id):
        """获取用户信息"""
        user = UserService.get_user_by_id(user_id)
        if not user:
            return jsonify({'error': '用户不存在'}), 404
        return jsonify(user.to_dict())
    
    def put(self, user_id):
        """更新用户信息"""
        data = request.json
        user = UserService.update_user(user_id, data)
        if not user:
            return jsonify({'error': '用户不存在'}), 404
        return jsonify(user.to_dict())
    
    def delete(self, user_id):
        """删除用户"""
        result = UserService.delete_user(user_id)
        if not result:
            return jsonify({'error': '用户不存在'}), 404
        return jsonify({'message': '用户已删除'})

class UserListResource(MethodView):
    def get(self):
        """获取所有用户"""
        users = UserService.get_all_users()
        return jsonify([user.to_dict() for user in users])
    
    def post(self):
        """创建新用户"""
        data = request.json
        
        # 验证必要字段
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'缺少必要字段: {field}'}), 400
        
        # 检查用户名是否已存在
        if UserService.get_user_by_username(data['username']):
            return jsonify({'error': '用户名已存在'}), 400
        
        # 创建用户
        user = UserService.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            is_admin=data.get('is_admin', False)
        )
        
        return jsonify(user.to_dict()), 201