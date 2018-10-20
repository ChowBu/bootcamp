from django.conf.urls import url

from bootcamp.feeds import views

urlpatterns = [
    # 展示feed流
    url(r'^$', views.feeds, name='feeds'),

    # 点击发布新feed
    url(r'^post/$', views.post, name='post'),

    # 点赞第一步，取消点赞
    url(r'^like/$', views.like, name='like'),

    # 点击comment
    url(r'^comment/$', views.comment, name='comment'),
    # 下拉刷新feeds
    url(r'^load/$', views.load, name='load'),
    url(r'^check/$', views.check, name='check'),
    url(r'^load_new/$', views.load_new, name='load_new'),

    # 点赞第二部，以及提交feed comment 第二部
    url(r'^update/$', views.update, name='update'),
    # comment第三步
    url(r'^track_comments/$', views.track_comments, name='track_comments'),
    # 删除评论或者feed
    url(r'^remove/$', views.remove, name='remove_feed'),
    #
    url(r'^(\d+)/$', views.feed, name='feed'),
]
