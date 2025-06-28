from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
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
    path('comment/<int:post_id>/', views.comment,),
    
]
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)