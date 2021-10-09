from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns = [
    # when it is empty means it is root url
    path('', views.index, name='index'),
    # when it is empty means it is root url
    path('counter/', views.counter, name='counter'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>/', views.post, name='post'),
    path('add_widget/', views.add_widget, name="add_widget"),
    path('forget_password/', views.forget_password, name="forget_password"),
    path('userInfo/', views.userInfo, name="userInfo")
    #path('reset_password/', views.password_reset_request, name="reset_password"),
]
