from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]