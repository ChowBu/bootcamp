from django.contrib import admin
from bootcamp.authentication.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # 不能添加tags 会出错，暂时不管
    # list_display = ('id','user','location', 'url','job_title',)
    # search_fields = ('user','location', 'url','job_title',)
    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    # list_editable = ('user','location', 'url','job_title',)