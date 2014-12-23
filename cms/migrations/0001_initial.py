# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'cms_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('is_nav', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.URLField')(default='http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg', max_length=120)),
        ))
        db.send_create_signal(u'cms', ['Category'])

        # Adding model 'Thing'
        db.create_table(u'cms_thing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.URLField')(default='http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg', max_length=120)),
        ))
        db.send_create_signal(u'cms', ['Thing'])

        # Adding model 'Post'
        db.create_table(u'cms_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(default=u'\u609f\u7f18', max_length=100, blank=True)),
            ('referer', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('pub_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_top', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('click', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Category'])),
            ('image', self.gf('django.db.models.fields.URLField')(default='http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg', max_length=120)),
        ))
        db.send_create_signal(u'cms', ['Post'])

        # Adding M2M table for field thing on 'Post'
        m2m_table_name = db.shorten_name(u'cms_post_thing')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'cms.post'], null=False)),
            ('thing', models.ForeignKey(orm[u'cms.thing'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'thing_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'cms_category')

        # Deleting model 'Thing'
        db.delete_table(u'cms_thing')

        # Deleting model 'Post'
        db.delete_table(u'cms_post')

        # Removing M2M table for field thing on 'Post'
        db.delete_table(db.shorten_name(u'cms_post_thing'))


    models = {
        u'cms.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg'", 'max_length': '120'}),
            'is_nav': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'cms.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'default': "u'\\u609f\\u7f18'", 'max_length': '100', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cms.Category']"}),
            'click': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg'", 'max_length': '120'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thing': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cms.Thing']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cms.thing': {
            'Meta': {'object_name': 'Thing'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'default': "'http://ww1.sinaimg.cn/large/67668a0fgw1em1cmjb5ouj20ak07qjrk.jpg'", 'max_length': '120'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['cms']