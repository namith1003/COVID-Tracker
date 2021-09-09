from django.urls import path
from home import views
app_name = 'home'
urlpatterns = [
    # when it is empty means it is root url
    path('', views.index, name='index'),
    # when it is empty means it is root url
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('signup', views.signup, name="signup"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),

]

# urlpatterns = [
#     # when it is empty means it is root url
#     path('', views.index, name='index'),
#     # when it is empty means it is root url
#     path('counter/', views.counter, name='counter'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('post/<str:pk>/', views.post, name='post'),
#     path('add_widget/', views.add_widget, name="add_widget"),
# ]
