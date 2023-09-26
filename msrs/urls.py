from django.urls import path
from django.contrib.auth import views as auth_views
from .views import FormWizardView, main
# from . import views

app_name = "msrs"

urlpatterns = [
  path("", main, name="home"),
  # path('form/', views.form, name='form'),
  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
  path('screening/<int:step>/', FormWizardView.as_view(), name='meu_form'),
]
