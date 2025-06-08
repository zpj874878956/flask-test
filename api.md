# Flask 版本管理系统 API 文档

本 API 文档涵盖了用户、产品、版本、文件等主要资源的接口说明，适用于 Web 前端对接。

接口地址：http://127.0.0.1:5000/api/v1
---

## 用户相关接口

### 获取所有用户
- **URL**: `/users`
- **方法**: GET
- **参数**: 无
- **返回**: 用户列表（JSON 数组）

### 创建新用户
- **URL**: `/users`
- **方法**: POST
- **参数**（JSON Body）:
  - `username` (string, 必填)
  - `email` (string, 必填)
  - `password` (string, 必填)
  - `is_admin` (bool, 选填)
- **返回**: 新建用户对象（JSON）

### 获取用户信息
- **URL**: `/users/<user_id>`
- **方法**: GET
- **参数**: 路径参数 `user_id`
- **返回**: 用户对象（JSON）

### 更新用户信息
- **URL**: `/users/<user_id>`
- **方法**: PUT
- **参数**（JSON Body）: 可更新字段
- **返回**: 更新后的用户对象（JSON）

### 删除用户
- **URL**: `/users/<user_id>`
- **方法**: DELETE
- **参数**: 路径参数 `user_id`
- **返回**: 删除结果（JSON）

---

## 产品相关接口

### 获取产品列表
- **URL**: `/products`
- **方法**: GET
- **参数**（Query）:
  - `page` (int, 选填)
  - `per_page` (int, 选填)
  - `status` (string, 选填)
- **返回**: 产品分页列表（JSON）

### 创建新产品
- **URL**: `/products`
- **方法**: POST
- **参数**（JSON Body）:
  - `name` (string, 必填)
  - `description` (string, 选填)
  - `code` (string, 必填)
  - `status` (string, 选填)
- **返回**: 新建产品对象（JSON）

### 获取产品详情
- **URL**: `/products/<product_id>`
- **方法**: GET
- **参数**: 路径参数 `product_id`
- **返回**: 产品对象（JSON）

### 更新产品信息
- **URL**: `/products/<product_id>`
- **方法**: PUT
- **参数**（JSON Body）: 可更新字段
- **返回**: 更新后的产品对象（JSON）

### 删除产品
- **URL**: `/products/<product_id>`
- **方法**: DELETE
- **参数**: 路径参数 `product_id`
- **返回**: 删除结果（JSON）

---

## 版本相关接口

### 获取版本列表（按产品）
- **URL**: `/versions`
- **方法**: GET
- **参数**（Query）:
  - `product_id` (int, 必填)
  - `page` (int, 选填)
  - `per_page` (int, 选填)
  - `status` (string, 选填)
- **返回**: 版本分页列表（JSON）

### 创建新版本
- **URL**: `/versions`
- **方法**: POST
- **参数**（JSON Body）:
  - `product_id` (int, 必填)
  - `version_number` (string, 必填)
  - `description` (string, 选填)
  - `release_notes` (string, 选填)
  - `author_id` (int, 必填)
  - `status` (string, 选填)
- **返回**: 新建版本对象（JSON）

### 获取版本详情
- **URL**: `/versions/<version_id>`
- **方法**: GET
- **参数**: 路径参数 `version_id`
- **返回**: 版本对象（JSON）

### 更新版本信息
- **URL**: `/versions/<version_id>`
- **方法**: PUT
- **参数**（JSON Body）: 可更新字段（不允许更改 product_id 和 author_id）
- **返回**: 更新后的版本对象（JSON）

### 删除版本
- **URL**: `/versions/<version_id>`
- **方法**: DELETE
- **参数**: 路径参数 `version_id`
- **返回**: 删除结果（JSON）

### 获取产品的版本历史
- **URL**: `/products/<product_id>/versions`
- **方法**: GET
- **参数**（Query）:
  - `page` (int, 选填)
  - `per_page` (int, 选填)
  - `status` (string, 选填)
- **返回**: 产品及其版本历史（JSON）

---

## 文件相关接口

### 上传文件
- **URL**: `/files/upload`
- **方法**: POST
- **参数**（form-data）:
  - `file` (file, 必填)
  - `version_id` (int, 必填)
  - `uploader_id` (int, 必填)
- **返回**: 文件对象（JSON）

### 下载文件
- **URL**: `/files/download/<file_id>`
- **方法**: GET
- **参数**: 路径参数 `file_id`
- **返回**: 文件流

### 获取版本的所有文件
- **URL**: `/files`
- **方法**: GET
- **参数**（Query）:
  - `version_id` (int, 必填)
- **返回**: 文件列表（JSON）

---

如需详细字段说明，请参考各资源的模型定义。 