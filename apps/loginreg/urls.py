from django.conf.urls import url, include
from .import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name = 'user_index'),
    url(r'^register$', views.register, name = 'user_register'),
    url(r'^bingo$', views.bingo, name = 'user_bingo'),
    url(r'^login$', views.login, name = 'user_login'),
    url(r'^logout$', views.logout, name = 'user_logout')
]
