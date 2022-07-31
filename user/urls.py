from django.urls import path
from user import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
]