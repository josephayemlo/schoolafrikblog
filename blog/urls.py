from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/admin', views.admin, name='admin'),
    path('blog/admin/new', views.blogpost_create, name='blogpost_create'),
    path('blog/admin/list', views.blogpost_list, name='blogpost_list'),
    path('blog/admin/<int:pk>/', views.blogpost_detail, name='blogpost_detail'),
    path('blog/admin/<int:pk>/edit/', views.blogpost_update, name='blogpost_update'),
     path('blog/admin//<int:pk>/delete/', views.blogpost_delete, name='blogpost_delete'),

]