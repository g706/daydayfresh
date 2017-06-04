from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail(\d+)/$', views.detail),
    url(r'^list(\d+)-(\d+)-(\d+)/$', views.list),
    url(r'^index_ajax(\d+)/$', views.index_ajax),
    url('^search/$', views.MySearchView()),

]