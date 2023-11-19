"""
URL configuration for IS241project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from AttendanceTracker import views
from django.views.generic.base import TemplateView
from AttendanceTracker.views import process_code, startclass

urlpatterns = [
    path('admin/', admin.site.urls),

    #login and registration    
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    #app function pages
    path('confirmation/', views.confirmation, name='confirmation'),
    path('courses/', views.courses, name='courses'),
    path('editcourse/', views.editcourse, name='editcourse'),
    path('reports/', views.reports, name='reports'),
    path('startclass/', views.startclass, name='startclass'),
    path('add_course/', views.add_course, name='add_course'),
    path('update_course/', views.update_course, name='update_course'),
    path('studcode/', process_code, name='studcode'),
    
    
]


