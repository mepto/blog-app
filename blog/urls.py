from django.urls import path, re_path
from . import views
# . import views means every view from the blog application

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
]
# or try re_path(r'^$', views.post_list, name='post_list'),
# path('', views.post_list, name='post_list'),
