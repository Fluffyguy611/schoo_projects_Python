from django.urls import path
import os
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='repository:index'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
]