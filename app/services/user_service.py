from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password, is_admin=False):
        """创建新用户"""
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            is_admin=is_admin
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user_by_id(user_id):
        """根据 ID 获取用户"""
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_username(username):
        """根据用户名获取用户"""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_all_users():
        """获取所有用户"""
        return User.query.all()
    
    @staticmethod
    def update_user(user_id, data):
        """更新用户信息"""
        user = User.query.get(user_id)
        if not user:
            return None
        
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password_hash = generate_password_hash(data['password'])
        if 'is_admin' in data:
            user.is_admin = data['is_admin']
        
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        """删除用户"""
        user = User.query.get(user_id)
        if not user:
            return False
        
        db.session.delete(user)
        db.session.commit()
        return True
    
    @staticmethod
    def verify_password(user, password):
        """验证用户密码"""
        if not user:
            return False
        return check_password_hash(user.password_hash, password)