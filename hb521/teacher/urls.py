from django.conf.urls import include, url
from django.contrib import admin
from  . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'hb521.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/',views.register),
    url(r'rg/',views.rg),
    url(r'^route/',views.route),
    url(r'^FAQ/',views.faq),
    url(r'add/',views.add),
    url(r'tijiao',views.tijiao,name='tj'),
    url(r'xianshi',views.xianshi),
    url(r'xq/(?P<pk>[0-9]+)',views.xq,name='xiangqing'),
    url(r'sc(?P<pk>\d+)',views.sc,name='shanchu'),
]
