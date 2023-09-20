from django.urls import path
from .views import FormWizardView, main
# from . import views

# not needed
# app_name = "blog"

urlpatterns = [
  path("msrs/", main, name="main"),
  # path('form/', views.form, name='form'),
  path('screening/<int:step>/', FormWizardView.as_view(), name='meu_form'),
]
