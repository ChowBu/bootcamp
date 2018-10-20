from django.contrib import admin
from bootcamp.feeds.models import Feed

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):

    list_display = ('id','user', 'date', 'post','parent','likes','comments')
    search_fields = ('post',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    list_editable = ('post',)


# 这样也可以，也可以像上面那样使用装饰器
# admin.site.register(Feed,FeedAdmin)
