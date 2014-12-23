from django.conf.urls import patterns, include, url
from cms import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dolulu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^ddadmin/', include(admin.site.urls)),
    url(r'^lanmu/(?P<pk>\d+)/$', views.category, name='category'),
    url(r'^$', views.index, name='index'),
    url(r'^meng/(?P<pk>\d+)/$', views.post, name='post'),
    url(r'search/$', views.search, name='search'),
)
