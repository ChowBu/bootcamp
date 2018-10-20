from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

import bleach

from channels import Group

from bootcamp.activities.models import Activity


@python_2_unicode_compatible
class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    # 递归，Feed的评论也是Feed
    parent = models.ForeignKey(
        'Feed', null=True, blank=True, on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    class Meta:
        # 对象的单数名字，没有的话对象类名会被拆分为名字
        # 这个名字的使用领域未知
        verbose_name = _('Feed')

        # 该对象复数形式的名称：
        verbose_name_plural = _('Feeds')
        # 对象的默认顺序
        # -表示正序，？表示随机(不加字段名)
        ordering = ('-date',)

    # 输出对象的时候显示的内容，为feed的post文章内容
    def __str__(self):
        return self.post

    # 静态方法，返回feed
    @staticmethod
    def get_feeds(from_feed=None):
        # 若指定了id的情况，找出小于这个id的，同时parent为none，则表示该feed
        # 为非评论
        if from_feed is not None:
            feeds = Feed.objects.filter(parent=None, id__lte=from_feed)

        else:
            feeds = Feed.objects.filter(parent=None)

        return feeds

    # 静态方法返回大于参数id的feeds
    @staticmethod
    def get_feeds_after(feed):
        feeds = Feed.objects.filter(parent=None, id__gt=feed)
        return feeds

    # 返回feed的评论，方法为返回parent为feed的feed,这就是当前评论
    def get_comments(self):
        return Feed.objects.filter(parent=self).order_by('date')

    def calculate_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk).count()
        self.likes = likes
        self.save()
        return self.likes

    def get_likes(self):
        likes = Activity.objects.filter(activity_type=Activity.LIKE,
                                        feed=self.pk)
        # likes = Feed.objects.filter(pk = self.pk).count()
        # print(type(likes))
        # print(dir(likes))
        return likes

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.user)
        return likers

    # 通过收集Feed里面parent为feed本身的feed计算comments的数目
    def calculate_comments(self):
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return self.comments

    # 通过user,post，以及parent为feed本身的id，存储feed为评论
    # 保存评论后计算评论数，然后返回评论
    def comment(self, user, post):
        feed_comment = Feed(user=user, post=post, parent=self)
        feed_comment.save()
        self.comments = Feed.objects.filter(parent=self).count()
        self.save()
        return feed_comment

    # 不知道干嘛的，应该是格式化文章post内容
    def linkfy_post(self):
        return bleach.linkify(escape(self.post))

    # webscoket这个是干嘛的暂时不清楚
    # 为什么把webscoket放到model里面这样做，也不清楚
    def feed_log(self, activity):
        Group('feeds').send({
            'text': json.dumps({
                'username': self.user.username,
                'activity': activity,
            })
        })


# 貌似是用来连接feed model 和post_save 的中间函数
# 每次有新的feed 产生了，就发送信息
def new_feed_added(sender, instance, created, **kwargs):
    if created:
        if instance.parent is None or instance.parent == "":
            instance.feed_log('new_feed')


post_save.connect(new_feed_added, sender=Feed)


# 何时使用staticmethod，何时使用实例方法

# 为何Feed 里面的方法获取Feed的内部信息用Feed，而不是使用self，无论是否为静态方法

# 为什么感觉有些model方法应该是view的逻辑，为什么把他们放到model？
# view 逻辑和model方法该如何界定？

# 为什么要把webscoket的实时逻辑放到model里面？
