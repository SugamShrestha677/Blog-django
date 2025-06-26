from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addBlog/', views.Blog),
    path('Preview/<int:post_id>/', views.preview),
    path('login/', views.login),
    path('signup/', views.signup),
    path('home/', views.home_page),
    path('delete/<str:id>', views.delete),
    path('edit/<str:id>', views.edit),
    
]
