from django.urls import path, re_path
from . import views
# . import views means every view from the blog application

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    #path('', views.handler404, name='404'),
    #path('', views.index, name='index'),
]
