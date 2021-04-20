from django.urls import path, re_path
from lists import views

urlpatterns = [
    path('new', views.new_list2, name='new_list'),
    re_path(r'^(\d+)/$', views.view_list, name='view_list'),
    re_path(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
