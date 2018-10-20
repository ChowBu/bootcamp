1. .env 文件只有对setting里面没有设置的参数有效
2. manage.py 默认采用的设置是 config.settings.local
3. 在关闭DEBUG 模式后无法访问静态资源
Django框架仅在开发模式下提供静态文件服务。开启DEBUG模式时，Django内置的服务器是提供静态文件的服务的，所以css等文件访问都没有问题，但是关闭DEBUG模式后，Django便不提供静态文件服务了

4. 使用whitenoise提供静态资源服务
setting加上以下内容

python3 pip
python3 -m pip install python_package
有requirements.txt的
python3 -m  pip install  -r  requirements.txt

```python 
MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE  # noqa F405
```

wsgi加上以下
```python
from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```
4. python manage.py collectstatic
这一句话就会把以前放在各个 app下static中的静态文件全部拷贝到 settings.py 中设置的 STATIC_ROOT 文件夹中


5. 使用setting.test2
去掉了django-debug-toolbar
速度显著提升了

6. boto3
是亚马逊云的环境

7. gunicorn 部署



8. 使用conf.setting.test2作为配置文件上线，导致有的密码么法登陆
因为增加了以下代码，导致密码验证方式变更，显示密码错误
```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
```


9. python3 manage.py collectstatic
搜集静态文件到 STATIC_ROOT 

10. STATIC_ROOT ,STATIC_URL,STATICFILES_DIRS 区别 MEDIA_ROOT以及MEDIA_URL
STATIC_ROOT，MEDIA_ROOT是用来存放文件的绝对路径，
STATIC_URL，MEDIA_URL则是使用文件的URL

11. 国际化
在local里面增加po，mo文件
+ local 表示地域文化的名称，可以是ll 格式的语种代码，
也可以是ll_CC 格式的语种和国家组合代码。
例如： it, de_AT, es, pt_BR. 。
语种部分总是小写而国家部分则应是大写，中间以下划线(_)连接。

+


# Django设置环境
```py
import os
import sys
sys.path.append("/Users/wangzhen/project/learning/python/jokes/jokes")
import requests
'''
这个脚本用于，新建一个Django项目之后，对于数据库进行其他操作
所以这里是个jokes.settings,因为我之前创建了一个叫做jokes的app
'''

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jokes.settings")
```


# Django 代替sql操作数据库

1. 进入shell环境 python3 manage.py shell
2. 导入模块的model 然后查询
```py
from polls.models import Question, Choice
# 查询所有的q
Question.objects.all()
# 查询参数arg为 
Question.objects.filter(arg)
```
3. 查询参考https://yiyibooks.cn/xx/django_182/topics/db/queries.html
 3.1 字段查询是指如何指定SQL WHERE 子句的内容。它们通过查询集方法filter()、exclude() 和 get() 的关键字参数指定。

查询的关键字参数的基本形式是field__lookuptype=value。（中间是两个下划线）
 3.2
 ```html
 __exact 精确等于 like ‘aaa’ 
__iexact 精确等于 忽略大小写 ilike ‘aaa’ 
__contains 包含 like ‘%aaa%’ 
__icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。 
__gt 大于 
__gte 大于等于 
__lt 小于 
__lte 小于等于 
__in 存在于一个list范围内 
__startswith 以…开头 
__istartswith 以…开头 忽略大小写 
__endswith 以…结尾 
__iendswith 以…结尾，忽略大小写 
__range 在…范围内 
__year 日期字段的年份 
__month 日期字段的月份 
__day 日期字段的日 
__isnull=True/False 
__isnull=True 与 __exact=None的区别
 ```
 3.3



# 使用reverse获取有两种方式
1. 通过url的name本例子，冒号之前是app的名字后面是url的名字，arg为参数
reverse('joke:post_detail', args=[str(self.id)])

2. 使用view
from news import views
reverse(views.archive)


# 生产url的两种方式
1. 在前端使用各个参数进行拼接
2. 使用 上面介绍的reverse 和get_absolute_url
```py
def get_absolute_url(self):
     reverse('joke:post_detail', args=[str(self.id)])
```



## 关于next跳转
1. account/edit 在未登陆的情况下，需要使用 login_required 传递next
2. joke/list?p=xx 在未登陆的情况下使用 传递next
```html
<input type="hidden" name="next" value="{% get_current_full_path request %}"/>
```


# 关于提交品论评论的实现的坑，很少
1. 需要提交非用户输入的内容，可以查看joke/views/post_detail.py 的提交用户名的实现

# 关于图片上传的实现
1. 图片上传除了要配置model意外还有
url的static  详细见jokes/urls.py


# 关于时区时区问题
1. Django 的时区问题 
setting.py 里面的
USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'
来控制

这样设置后存储的时间少了8个小时但是，实际上时间是带有时区的，在展示的时候会根据时区来展示
因此数据展示的时候是对的

在设置了USE_TZ=True之后，如果设置了TIME_ZONE = 'Asia/Shanghai'，
尽管数据库中存储的是UTC时间，但在模板显示的时候，会转成TIME_ZONE所示的本地时间进行显示。
存储到数据库中的时间比本地时间会小8个小时的原因。


建议：为了统一时间，在django开发时，尽量使用UTC时间，即设置USE_TZ=True，
TIME_ZONE = 'Asia/Shanghai'，并且在获取时间的时候使用django.util.timezone.now()。
因为后台程序使用时间时UTC时间就能满足，也能保证证模板时间的正确显示。



# 数据库操作
将空格右边的数据删除
有bug 没有考虑，没有空格的情况
```sql
UPDATE ltrimtest SET user = replace(user,locate('\n',user))
```

去掉数据库字段内部的 空格 换行 符号
joke_airticle_pack表名
user 字段
```sql
UPDATE joke_airticle_pack SET user = REPLACE(REPLACE(user, CHAR(10),''), CHAR(13),'');
```

# postgresql数据库 导入 .sql 文件
 psql -U wangzhen -d geodjango -f /Users/wangzhen/project/bootcamp/bootcamp/baidu_auth_user.sql
-U 后面为用户 -d 后面为数据库名 -f 为文件路径




# postgresql 在bootcamp 使用insert导入数据后，会出现sequences与主键不匹配的情况
导致 家属数据可能出现pk  exist的情况，正确的处理方式是导入数据后
更改序列的现有值 推荐pgadmin 可视化更改

# bootcamp的user 和profile 表的id 与 user_id内容一定要一一对上，否则会出现无法评论
以及无法注册的情况


# mysql 将一个表复制到另外一个表
```
INSERT INTO auth_profile SELECT * FROM auth_profile_temp



1. 表结构完全一样
  insert into 表1
  select * from 表2
2. 表结构不一样（这种情况下得指定列名）
  insert into 表1 (列名1,列名2,列名3)
select 列1,列2,列3 from 表2

3.不同数据库，需要在表前面加数据库前缀，database.表名。

注意：以上测试过OK，sql语句不需要在insert后面加values。

```


# mysql 密码忘记，或者更改密码无法登陆
https://blog.csdn.net/pariese/article/details/77527813
```
第一种
mysql版本：5.7.17
1.首先我们要关闭mysql服务
sudo /usr/local/mysql/support-files/mysql.server stop
2.我们要用安全模式启动mysql
sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables
3.使用root账号登录mysql服务
/usr/local/mysql/bin/mysql u root
4.修改root账号的密码（其实这运行的是sql语句）
update mysql.user set authentication_string='qingyun1' where user='root' and Host = 'localhost';
update mysql.user set password='qingyun1' where user='root' and Host = 'localhost';
如果有必要，建议运行一下:flush privileges;
5.关闭安全模式，正常的重启mysql
sudo /usr/local/mysql/support-files/mysql.server restart
6.正常的使用root账号和密码连接mysql
/usr/local/mysql/bin/mysql -u root -p
第二种
如果忘记密码,强行修改:
1： 停止Mysql服务 sudo /usr/local/mysql/support-files/mysql.server stop
2： 进入终端输入：cd /usr/local/mysql/bin/ 回车后;
登录管理员权限 sudo su 回车后;
输入以下命令来禁止mysql验证功能 ./mysqld_safe --skip-grant-tables &  回车后mysql会自动重启（偏好设置中mysql的状态会变成running）
3.   输入命令 ./mysql 回车后，
输入命令 FLUSH PRIVILEGES;
   回车后，输入命令 ALTER USER 'root'@'localhost' IDENTIFIED BY '你的新密码';
第三种
1.  停止 mysql server.  通常是在 '系统偏好设置' > MySQL > 'Stop MySQL Server'
或者: sudo /usr/local/mysql/support-files/mysql.server stop
2.  打开终端，输入：
     sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables
3.  打开另一个新终端，输入:
     sudo /usr/local/mysql/bin/mysql -u root
     UPDATE mysql.user SET authentication_string=PASSWORD('新密码') WHERE User='root';
     FLUSH PRIVILEGES;
     \q
4.  重启 sudo /usr/local/mysql/support-files/mysql.server restart
*以上方法针对 mysql V5.7.9, 旧版的mysql请使用：UPDATE mysql.user SET Password=PASSWORD('新密码') WHERE User='root';
```


todo
1. 下一页
<!--下一页实现，在详情页面里面，具体优化见注释-->
2. 点赞
3. 邮箱注册，
4. 邮箱重置密码
5. QQ 微信直接登陆验证
6. tag
7. home 页面包含了 profile 会导致未登录时报错，可以在登陆页面去掉设置
那几行







# Django python3 使用mysql
直接按照内置安装的话就会提示安装mysqlclient 或者...
同时在project 的主App的__init__.py 加入
import pymysql
pymysql.install_as_MySQLdb()

# 使用 python3 manage.py inspectdb 依据数据库生成Model

# django 数据备份
python3 manage.py dumpdata app_name.my_model --format=json > app.json

将名为app_name 的app的my_model 导出格式为json 的app.json

# 数据导入使用，Python命令行导入数据，教程在 import_tutorial.py

# mysql manage.py makemigrations 可能无法创建数据库
直接使用manage.py sqlmigrate appname 0001(其他等等序号)

# mysql 命令行 执行语句需要在语句后面加上分号

# mysql 设置默认的编码存储中文
分为两种情况
1. 新建的表 修改  /usr/local/etc 下的my.cnf ；
路径下没有的话，就新建一个模版在/usr/local/mysql/support-files
2. 原有的表在 字段后面加上 character set utf8  没有-




https://blog.csdn.net/u013145194/article/details/51527389
http://jessej.blog.163.com/blog/static/6501024820139130509860/
# 设置mysql 支持表情编码
使用语句查看支持情况 SHOW VARIABLES WHERE Variable_name LIKE 'character_set_%' OR Variable_name LIKE 'collation%'

一、修改mysql server

改配置文件/etc/my.cnf（window为my.ini）

[client]

default-character-set = utf8mb4

[mysql]

default-character-set = utf8mb4

[mysqld]

character-set-client-handshake = FALSE

character-set-server = utf8mb4

collation-server = utf8mb4_unicode_ci

init_connect='SET NAMES utf8mb4'

注意：mysql支持utf8mb4的版本是5.5.3+，必须升级到较新版本

查看版本：SHOW VARIABLES WHERE Variable_name LIKE ‘version%’;

执行数据库和表、字段的字符集sql:

数据库  ALTER DATABASE 数据库名 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE 表名 CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


alter table t_yown_user modify `NICKNAME` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci COMMENT '昵称';

ALTER TABLE user_comments CHANGE content content TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


# 整个Django的架构
1. model为数据来源
2. view 定义传递进templates的数据，以及交互，绑定渲染的模板以及与之对应的数据
3. templates 为视图模板，渲染view传递进去的数据
3.1. template 数据来源
  1. 指定模板的view.py 对应的数据
  2. URL 参数的name
  3. 自定义的标签过滤器

# sql迁移 命令
1. python3 manage.py makemigrations appname

生产序号 0000X

2. python3 manage.py sqlmigrate appname 0000X

3. python3 manage.py migrate


# 新建项目后，创建超级用户
python3 manage.py createsuperuser


## 删除对象也将删除任何的依赖关系

## 默认约定所有的模版都是在 templates里面，同时template里面建立一个与app同名的文件夹 也可以不这样做，但是不推荐


## Django 新建项目后

## 数据库启动
pg_ctl start -D  PGDATA  -l logfile

#这里使用 createdb geodjango  -U wangzhen

# psql -U wangzhen -d geodjango -h 127.0.0.1 -p 5432 登录用户啊
user database host port


# templates
1. 如何将变量穿进template
2. 怎么将变量组织，符合传进template的规范
3. 静态文件的组织规范
* {% extends "base.html" %} 
 同级别下直接使用（见account），不同级别加上文件夹（见blog）
* {% load staticfiles %}
* 上级被包含的页面包括了 content 下级的页面包含content 两者用来互相包含


## registration
auth
创建一个新的目录命名为registration。这个路径是Django认证（authentication）视图（view）期望你的认证（authentication）模块（template）
默认的存放路径。在这个新目录中创建一个新的文件，命名为login.html

# 模型字段类型有哪些？
1. 全都在源码的 django/db/model/fields/__init__ pycharm生成digram 后查看
2. 各个字段的参数 上文的各个类的__init__的参数，以及父类的__init__参数
3. 继承模型的默认属性
3. 自定义Model 
4. 各个字段默认会生成 "app名称"_"类名"
5. 会自动增加ID字段
6. 以下子类里面类似ordering 的属性还有哪些方法
class Meta:
       ordering = ('created',)
Django的模型class Meta在 Django/db/model/options.py 里面

     
        
7. 以下类似__str__(self): 的方法还有哪些
  def __str__(self):
  
8. 关联关系有哪些？以及其参数
django/db/model/fields/related.py

# 模型的增删CRUD
1. C 创建Model python3 manage.py makemigrations python3 manage.py migrate
2. R admin.py 增加查看的模型，即可后台查看
3. U 直接修改Model python3 manage.py makemigrations python3 manage.py migrate
4. 如何删表 ？

# 模型的扩展account/model.py.profile
两个对象如何扩展
扩展的时候如何为被扩展的model设置默认值


扩展模型的时候，出现了，user为空的情况，edit页面抛出了
 RelatedObjectDoesNotExist

# Migration socialaccount.0001_initial dependencies reference nonexistent parent node ('sites', '0001_initial')
contri/sites下面没有 0001_initial.py 这个
这个是哪里来的？为什么初始化就有，难道是从原生代码扒过来的

# geojson 和 shp 互转
最好采用opengis 的 shp2psql

# 社交认真设置allowhost 
 1. 因为社交认证不允许127.0.0.1,所以需要修改mac下的
 编辑你的/etc/hosts文件添加如下内容，
 127.0.0.1 mysite.com 
 因为权限问题出现不允许修改的话，使用 显示简介修改写入写出权限
 2. 在settings 文件下的allowhost数组下加上'mysite.com'
 
 # 多对多关系 ManyToManyField
 当你定义一个ManyToMany字段时，Django 会用两张表主键（primary key）创建一个中介联接表
 （译者注：就是新建一张普通的表，只是这张表的内容是由多对多关系双方的主键构成的）。
 ManyToMany字段可以在任意两个相关联的表中创建。
同ForeignKey字段一样，ManyToMany字段的related_name属性使我们可以命名另模型回溯（或者是反查）
到本模型对象的关系。ManyToMany字段提供了一个多对多管理器（manager），
这个管理器使我们可以回溯相关联的对象比如：image.users_like.all()或者从一个user中回溯，
比如：user.images_liked.all()。


# 决定使用具体哪一个配置文件conf由manage.py决定,

pycharm 内存占用高
1. 包含的文件夹太深，类似npm包的嵌套
2. 打开的文件，文件夹嵌套太深，类似查看定义的时候的跳转
2. 打开的文件，文件夹嵌套太深，类似查看定义的时候的跳转


# virtualenv 的使用安装 
1. 创建直接使用pycharm 在环境里面创建local 环境 获取路径位置 env
2. cd env （进入虚拟环境）
3. 运行source env/bin/activate 即可激活

4.  这样就可以在目前路径下运行各种python 命令 比如 python3 -m pip install -r requirements.txt



# 视图层总结
### 返回可为
1. http
### django.http 主要为对于各种状态的封装，以及返回内容的封装，比如返回csv,json文件

# postgresql数据库 导入 .sql 文件
 psql -U wangzhen -d geodjango -f /Users/wangzhen/project/bootcamp/bootcamp/baidu_auth_user.sql


# 数据库互转

# 关于bootcamp 的feeds_feed



# mysql 转化pgsql  主要问题，去掉单引号，以及反斜杠和单引号一起\'
