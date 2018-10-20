from django.contrib import admin
from bootcamp.activities.models import Activity,Notification

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = ('user','activity_type', 'date', 'feed','question','answer',)
    search_fields = ('user','activity_type', 'date', 'feed','question','answer',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    # list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    list_editable = ('feed',)




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    # list_display = ('from_user','to_user', 'date', 'feed','question','answer','article','notification_type','is_read',)
    # search_fields = ('from_user','to_user', 'date', 'feed','question','answer','article','notification_type','is_read',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    # list_editable = ('feed',)



# 这样也可以，也可以像上面那样使用装饰器
# admin.site.register(Activity,ActivityAdmin)
# admin.site.register(Notification,NotificationAdmin)
