"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, fill_step, final_step

urlpatterns = [
    path("<str:type_form>/<int:step>/", fill_step, name="forms_steps"),
    path("<str:type_form>/final/", final_step, name="forms_final_step"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", index, name="home"),
]
