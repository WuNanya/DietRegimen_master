这里放项目相关的东西
# 食疗养生说明文档

---

## 数据库、数据字典

### 用户表：user
字典 | 命名 | 数据类型 | 说明 
---|---|---|---
用户id |user_id|int(16)|自增，主键
用户名|username|char(16)|不允许重复
密码|password|char(20)|
手机号|tel|
邮箱|email|
性别|sex|
出生日期|birth|
注册时间|register_time|
最后登录时间|last_login|

### 菜品表：food
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
菜品id|food_id
菜品名字|food_name| |不允许重复
菜品描述|	food_info| | 
菜品做法|	food_make| |
菜品图片|	food_img| |	（存本地路径）
点击数|click_num|int|每次点击自动加一
收藏数|collect_num|int|每收藏自动加一

### 食谱表：menu
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
食谱id|menu_id
用户id|user_id
食谱名称|menu_name


### 食谱-标签表：menu_tag
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
食谱id|		menu_id
标签id|		tag_id
是否有效|effective

### 标签表 ：tag
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
标签id |		tag_id
标签名	|	tag_name
是否有效|effective
点击数|click_num|int|每有人点击此类标签菜品自动加一

### 用户收藏表：collect
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
用户id	|	user_id
菜品id	|	food_id

### 食谱-菜品表：menu_food
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
食谱id|menu_id| | 
菜品id|food_id| | 菜品是用户自己添加进这个食谱的

### 菜品-标签表：food_tag
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
菜品id|food_id
标签id|tag_id 

### 历史足迹表
字段 | 命名 | 数据类型 | 说明 
---|---|---|---
用户id|
菜品id|
浏览时间|click_time|Date

### 用户-标签表
字段 | 命名 | 数据类型 | 说明
---|---|---|---
用户id|
标签id|
点击数|click_num|int|每点击此类标签菜品自动加一
收藏数|collect_num|每收藏自动加一



## 功能点接口说明

### 登录，注册与找回密码

#### 登录
- url:http://local/login
- 请求方法：POST
- 参数：
    - 账号: username
    - 密码：password
- 返回值：返回渲染后的首页

#### 注册
- url：http://local/register
- 请求方式：POST
- 请求参数：
    - 账号：username（唯一）
    - 密码：password
    - 手机号：phone_num
    - 邮箱：email
- 返回值：登录页面

#### 找回密码
- url：http://local/find-password
- 请求方式：POST
- 请求参数：
    - 账号 username
    - 手机号 phone_num
    - 新密码 password
    - 验证码 ver_code
- 返回值：登录页面

### 首页
#### 搜索
- url:http://local/search
- 请求方法：POST
- 参数：
  - 关键字key
- 返回值：根据关键字搜索出的食物渲染后的页面

#### 拍照
- url:http://local/photo
- 请求方法：POST
- 参数：
  - 照片photo
- 返回值：解析拍照数据后的页面

#### 滑动广告
- url:http://local/home
- 请求方法：GET
- 参数：无
- 返回值：n个广告列表（图片）包含链接

#### 热门菜品（进入时）
- url:http://local/home
- 请求方法：GET
- 参数：无
- 返回值：热门的n个菜品（食物）

#### 热门菜品的刷新按钮
- 换一批推荐菜品
- url:http://local/changefood
- 请求方法：POST
- 参数：现有菜品的id的列表
- 返回值：依然返回主页面，不过菜品列表重新渲染，不出现之前有的

#### 单个菜品
- url:http://local/single/1
- 请求方法：GET
- 参数：
  - 菜品（食物）id
- 返回值：
  - 食物名称
  - 食物功效列表
  - 食物做法文本
  - 食物图片

### 食谱
#### 食谱列表
- 请求页面返回自己的所有食谱
  - url:http://local/recipe
  - 请求方式：get
  - 参数：无
  - 返回值：
    - 食谱列表：
      - 食谱标签列表
      - 食谱剩余时间
      - 食谱推荐3个菜的列表
  - 说明：返回3个菜是系统做出的推荐，格式为食谱列表里包含一个字典，字典里的key值分别是：‘标签’，‘剩余天数’，‘食品推荐’，value值分别是：列表，int，列表

#### 点进单个食谱页面
- url:http://local/recipe-detail/1
- 请求方式：get
- 参数：食谱id
- 返回值：
  - 食谱标签列表
  - 食谱推荐的所有菜品列表
- 说明：url的1是用户的第一个食谱

#### 删除食谱标签
- url:http://local/recipe-detail/1
- 请求方式：DELETE
- 参数：标签id
- 返回值：
  - status：成功与否的状态
  - msg：信息
- 说明：url的1就是用户的第一个食谱

#### 添加食谱标签

## 我的
#### 基本信息
- 获取头像
  - url:http://local/mine
  - 请求方式：get
  - 参数：无
  - 返回值：渲染后的我的页面

#### 足迹
- 查看历史足迹
  - url:http://local/history
  - 请求方式：get
  - 参数：无
  - 返回值：

#### 收藏
- 取消收藏
  - url:http://local/collection
  - DELETE
  - 参数：
    - 食物id
- 添加收藏
  - url:http://local/collection
  - POST
  - 参数：
    - 食物id

#### 设置
- 退出账户
  - url:http://local/quit
  - POST
  - 参数：无，从session获取用户信息并且清除，同时记录最后一次登出时间
- 反馈帮助
  - 提交咨询、建议、其他
    - url:http://local/feedback
    - POST
    - 参数：
      - type类型：咨询consult、意见opinion、其他other之一
      - content内容：不超过300字
      - e_mail：邮箱格式
      - contact：联系方式（手机或者qq）
