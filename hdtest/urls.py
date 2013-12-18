from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hdtest.views.index_view', name='index'),
    url(r'^posts/', include('hdtest.posts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
