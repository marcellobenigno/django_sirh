from django.conf.urls import url
from sirh.basins import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add/$', views.create, name='add'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),
]