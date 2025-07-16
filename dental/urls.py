"""
URL configuration for dental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import landing_view
from user_dash.views import submit_report_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='landing'), 
    path('accounts/', include('accounts.urls')),
    path('dash/user/', include('user_dash.urls')),
    path('dash/dentist/', include('dentist_dash.urls')),
    path('/submit_report/', submit_report_view, name='submit_report'),  # Assuming this is for submitting test reports
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
