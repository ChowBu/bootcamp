from django.contrib import admin
from bootcamp.articles.models import Article,ArticleComment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 不能添加tags 会出错，暂时不管
    list_display = ('title','slug',  'content','status','create_user',)
    search_fields = ('title','slug',  'content',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    list_editable = ('content','status',)

@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):

    # list_display = ('id','article','comment', 'date', 'user',)
    search_fields = ('id','article','comment', 'date', 'user',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    # list_editable = ('article','comment', 'user',)


# 这样也可以，也可以像上面那样使用装饰器
# admin.site.register(Article,ArticleAdmin)
# admin.site.register(ArticleComment,ArticleCommentAdmin)
