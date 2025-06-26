from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page),
    path('addBlog/', views.Blog),
    path('Preview/<int:post_id>/', views.preview),
    path('login/', views.login),
    path('signup/', views.signup),
    
]
