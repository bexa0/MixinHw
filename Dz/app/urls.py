from django.urls import path

from app import views

urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('register/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('signup', views.SignUp.as_view(), name='register'),
    path('login', views.LoginForm.as_view(), name='login'),
]