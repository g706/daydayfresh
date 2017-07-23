
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register),
    url(r'^register_hanld/$', views.register_hanld),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login_hander/$', views.login_hander),
    url(r'^logout/$', views.logout),
    url(r'^info/$', views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),

]
