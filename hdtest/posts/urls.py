from django.conf.urls import patterns, url

urlpatterns = patterns('hdtest.posts.views',
    url(r'^(?P<post_id>\d+)/$', 'read_post_view', name='post-read'),
)