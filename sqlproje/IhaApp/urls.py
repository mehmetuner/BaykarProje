from django.urls import re_path as url
from IhaApp import views
urlpatterns = [
    url(r'^ihadata$',views.ApiIha),
    url(r'^ihadata/([0-9]+)$', views.ApiIha),
 
    url(r'^user$',views.user_login),
    url(r'^user/([0-9]+)$', views.user_login),
    
    url(r'^useriha$',views.ApiUserWindowIha),
    url(r'^useriha/([0-9]+)$', views.ApiUserWindowIha),
    
]
