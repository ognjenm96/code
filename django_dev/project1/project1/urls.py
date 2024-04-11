"""
URL configuration for project1 project.

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
from django.urls import path
from django.urls import include 

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('app_one/', include('app_one.urls')),
    path('nova_godina/', include('nova_godina.urls'))
] # This line includes the URL configuration for the app_one app. The include() function is used to include the URL configuration from another URLconf module. In this case, the URL configuration for the app_one app is included by passing the app_one.urls module to the include() function. This means that any URL patterns defined in the app_one.urls module will be included in the URL configuration for the project1 project. The URL pattern for the app_one app is 'app_one/'. This means that any URL patterns defined in the app_one.urls module will be prefixed with 'app_one/' in the project1 project. For example, if the URL pattern in the app_one.urls module is an empty string, it will be accessible at 'app_one/'. If the URL pattern is 'index/', it will be accessible at 'app_one/index/'.