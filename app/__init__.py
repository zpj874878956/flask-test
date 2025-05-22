from flask import Flask
from flask_cors import CORS
from app.api import api_bp

def create_app(config_class=None):
    app = Flask(__name__)
    
    # 配置应用
    if config_class:
        app.config.from_object(config_class)
    
    # 初始化扩展
    # 添加CORS支持
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 注册蓝图
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    return app