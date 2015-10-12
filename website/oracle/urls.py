from django.conf.urls import patterns, url, include
from rest_framework import routers
from oracle import views

router = routers.DefaultRouter()
router.register(r'oraclelist', views.OracleListViewSet)


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pages/', views.pages, name='pages'),
    #url(r'^$', include(router.urls)),
    url(r'^test$', views.test, name='test'),
    url(r'^mssql$', views.mssql, name='mssql'),
    url(r'^sop$', views.sop, name='sop'),
    #url(r'^ueditor$',include('DjangoUeditor.urls' )),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^sop/(.*)$', views.blog_sop, name='blog_sop'),
    url(r'^scanport$', views.scanport, name='scanport'),
    url(r'^scanresult/$',views.scanresult, name='scanresult'),
    url(r'^alert_event/$',views.alert_event, name='alert_event'),
    url(r'^add_event/$',views.add_event, name='add_event'),
    url(r'^oracle_command/$',views.oracle_command, name='oracle_command'),
    url(r'^diskspace/$',views.diskspace, name='diskspace'),
    url(r'^commandresult/$',views.commandresult, name='commandresult'),
    url(r'^oracle_status$',views.oracle_status, name='oracle_status'),
    url(r'^oracle_status2$',views.oracle_status2, name='oracle_status2'),
    url(r'^check_graphic$',views.check_graphic, name='check_graphic'),
    url(r'^check_hitratio$',views.check_hitratio, name='check_hitratio'),
    url(r'^performance$',views.performance, name='performance'),
    url(r'^check_topsql$',views.check_topsql, name='check_topsql'),
    url(r'^highcharts$',views.highcharts, name='highcharts'),
    url(r'^os_performance$',views.os_performance, name='os_performance'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url( r'^highcharts/js/(?P<path>.*)$', 'django.views.static.serve',
 #           { 'document_root': '/ezio/website/oracle/highcharts/js' }
  #  ),  
)



