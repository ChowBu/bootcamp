from django.contrib import admin
from bootcamp.questions.models import Question,Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # 因为某些属性（比如date，也可能是user）不便搜索，可能会报以下错误
    # Related Field got invalid lookup: icontains
    list_display = ('user','title', 'description', 'update_date','votes','favorites','has_accepted_answer',)
    search_fields = ('title', 'description', 'update_date','votes','favorites','has_accepted_answer',)

    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    list_editable = ('description',)



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ('user','question', 'description', 'create_date','update_date','votes','is_accepted',)
    search_fields = ('user','question', 'description', 'create_date','update_date','votes','is_accepted',)

    # 设置列表页展示条目数比较小，可提高打开列表页性能
    list_per_page = 10
    # list_filter是性能杀手，尽量不要开启
    # list_filter = ('user',  'post',)
    # 开始没有加id进入list_display导致第一项title没法编辑，出现以上问题，后来加了个id在前面解决
    list_editable = ('description',)





# 这样也可以，也可以像上面那样使用装饰器
# admin.site.register(Feed,FeedAdmin)

# admin.site.register(Feed,FeedAdmin)


