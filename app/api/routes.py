from app.api import api_bp
from app.api.resources.user import UserResource, UserListResource
from app.api.resources.file import FileUploadResource, FileDownloadResource
from app.api.resources.version import VersionResource, VersionListResource, VersionHistoryResource
from app.api.resources.product import ProductResource, ProductListResource

# 用户资源路由
api_bp.add_url_rule('/users', view_func=UserListResource.as_view('user_list'))
api_bp.add_url_rule('/users/<int:user_id>', view_func=UserResource.as_view('user'))

# 文件资源路由
api_bp.add_url_rule('/files/upload', view_func=FileUploadResource.as_view('file_upload'))
api_bp.add_url_rule('/files/download/<int:file_id>', view_func=FileDownloadResource.as_view('file_download'))

# 产品资源路由
api_bp.add_url_rule('/products', view_func=ProductListResource.as_view('product_list'))
api_bp.add_url_rule('/products/<int:product_id>', view_func=ProductResource.as_view('product'))

# 版本资源路由
api_bp.add_url_rule('/versions', view_func=VersionListResource.as_view('version_list'))
api_bp.add_url_rule('/versions/<int:version_id>', view_func=VersionResource.as_view('version'))
api_bp.add_url_rule('/products/<int:product_id>/versions', view_func=VersionHistoryResource.as_view('version_history'))