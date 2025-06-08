from flask import Flask
from flask_cors import CORS
from app.extensions import init_extensions
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # 配置应用
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # 初始化扩展
    init_extensions(app)
    
    # 添加CORS支持
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 注册蓝图
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    return app