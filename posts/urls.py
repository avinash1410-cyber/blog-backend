from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<int:pk>/', views.post, name='p_post'),
    path('create_post/', views.create_post, name='index'),
    path('login/', views.log, name='log'),
    path('post_post/<int:pk>', views.add, name='log'),
]