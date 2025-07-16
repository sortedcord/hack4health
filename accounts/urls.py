from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_dentist, role_dashboard_redirect

from accounts.views import landing_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/dentist/', register_dentist, name='register_dentist'),
    path('role-redirect/', role_dashboard_redirect, name='role_dashboard_redirect'),
]