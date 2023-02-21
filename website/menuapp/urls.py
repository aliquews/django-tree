from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^home/$', views.index, {'name': 'Home page'}, name='index'),
]