from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__)

# 添加处理CORS预检请求的路由
@api_bp.route('/', methods=['OPTIONS'])
@api_bp.route('/<path:path>', methods=['OPTIONS'])
def handle_options_request(path=None):
    return jsonify({"status": "ok"}), 200

from app.api import routes
