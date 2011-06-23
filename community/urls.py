from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^minar-sidur/baeta-vid-efni/ny-grein/$', 'community.articles.new'),
	url(r'^minar-sidur/baeta-vid-efni/nyr-vefsidutengill/$', 'community.bookmarks.new'),

	url(r'^minar-sidur/mitt-efni/greinasafn/$', 'community.articles.mine'),
	url(r'^minar-sidur/mitt-efni/tenglasafn/$', 'community.bookmarks.mine'),

	url(r'^greinasafn/(?P<user>[^/]*)/(?P<slug>[^/]*)/$', 'community.articles.view', name='view-article'),
	url(r'^tenglasafn/(?P<user>[^/]*)/(?P<slug>[^/]*)/$', 'community.bookmarks.view', name='view-bookmark'),

        url(r'^greinasafn/$', 'community.articles.all'),
        url(r'^tenglasafn/$', 'community.bookmarks.all'),
)

