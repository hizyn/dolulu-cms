#coding=utf-8
from django.db import models
from datetime import datetime

STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'已删',    
}

class Category(models.Model):
    title = models.CharField(u'名称', max_length=40)
    keywords = models.CharField(u'关键词', max_length=80, blank=True)
    description = models.CharField(u'描述', max_length=200, blank=True)
    is_nav = models.BooleanField(u'是否在导航位置显示', default=False)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items())
    image = models.URLField(u'缩略图', max_length=120, default="http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg")

    class Meta:
        verbose_name_plural = verbose_name = u'分类'

    def __unicode__(self):
        return self.title


class Thing(models.Model):
    title = models.CharField(u'名称', max_length=40)
    keywords = models.CharField(u'关键词', max_length=80, blank=True)
    description = models.CharField(u'描述', max_length=200, blank=True)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items())
    image = models.URLField(u'缩略图', max_length=120, default="http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg")

    class Meta:
        verbose_name_plural = verbose_name = u'标签'

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(u'标题', max_length=40)
    keywords = models.CharField(u'关键词', max_length=80, blank=True)
    description = models.CharField(u'描述', max_length=200, blank=True)
    author = models.CharField(u'作者', max_length=100, blank=True, default=u'悟缘')
    referer = models.CharField(u'来源', max_length=100, blank=True)
    content = models.TextField(u'正文')
    pub_time = models.DateTimeField(u'发表时间', default=datetime.now)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    is_top = models.BooleanField(u'是否置顶', default=False)
    status = models.IntegerField(u'状态', default=0, choices=STATUS.items())
    click = models.IntegerField(u'点击量', default=0)
    category = models.ForeignKey(Category, verbose_name=u'栏目')
    thing = models.ManyToManyField(Thing)
    image = models.URLField(u'缩略图', max_length=120, default="http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg")

    class Meta:
        verbose_name_plural = verbose_name = u'文章'

    def __unicode__(self):
        return self.title
