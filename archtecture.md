# 数据导入流程
1. 创建一个表结构和目标表一模一样
2. 使用jokes的 import_export脚本把数据从爬虫数据库导出到临时表格
3. 将临时表格的数据导出为 .sql 文件
4. 将.sql 文件插入到 目标数据库


# 数据库设计  前后端不分离的情况下如何在列表页，而不是详情页展示有的评论，（类似糗事百科和最右的神评论）
使用数据库的递归具体可见Feed的model实现


# template 以及与之相关的
1. partial_feed.html  csrf_token 是干嘛的，以及怎么出现在template的
1、    csrf在ajax提交的时候通过请求头传递的给后台的

2、    csrf在前端的key为：X-CSRFtoken，到后端的时候django会自动添加HTTP_,并且最后为HTTP_X_CSRFtoken

3、    csrf在form中提交的时需要在前端form中添加{%csrftoken%}



2. partial_feed.html  {% url 'profile' feed.user.username %} url反解
profile 为url.py 内url的name 后面的feed.user.username为 传入的参数

3. partial_feed.html  humanize naturaltime 时间格式
safe 

4. partial_feed.html  {% comment %} Place holder to load feed comments {% endcomment %}
 这是什么删了，也没事
 
5. 各个?后面的querystring哪里来的？
