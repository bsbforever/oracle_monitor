from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'website.views.home', name='home'),
    url(r'^$', 'oracle.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^oracle/', include('oracle.urls')),
    url(r'^oracle/', include('oracle.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
