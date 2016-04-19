from django.conf.urls import url
from sirh.basins import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]