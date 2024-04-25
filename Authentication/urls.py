from django.urls import path
from . import views
from .views import login, register_user

urlpatterns = [
    path('api/register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', views.UserLoginView.as_view(), name='user-login'),
    path('api/logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('login/', login, name='login'),
    path('register/', register_user, name='register')
]