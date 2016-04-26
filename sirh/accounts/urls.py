from django.conf.urls import url
from sirh.accounts import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login_form.html'}, name='login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': 'home'}, name='logout'),
]
