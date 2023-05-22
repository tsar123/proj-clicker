from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]