from django.conf.urls import patterns, include, url
from django.contrib import admin
from oauthtest.oaut.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oauthtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/env/$',ListCreateEnvelope.as_view(),name="list_create_view"),
    url(r'^api/users',ListCreateUser.as_view(),name="list_create_user"),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/env/(?P<pk>[0-9]+)/$', RetrieveUpdateDestroy.as_view(),name="one"),
)
