from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',name='client'),
    #url(r'^viewmatrix$', views.clientinfo, name='view'),
    #url(r'^student.html$', views.student, name='client'),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
]

