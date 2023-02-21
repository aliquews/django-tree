from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^index/$', views.index, {'name': 'Home page'}, name='index'),
    re_path(r'^company/$', views.index, {'name': 'Company'}, name='company'),
    re_path(r'^company/about_us$', views.index, {'name': 'About us'}, name='about_us'),
    re_path(r'^company/career$', views.index, {'name': 'Career'}, name='career'),
    re_path(r'^shop/$', views.index, {"name": "Shop"}, name='shop'),
    re_path(r'^shop/computers$', views.index, {"name": "Computers"}, name='computers'),
]