from django.urls import path
from django.contrib.auth import views as auth_views
from .views import FormWizardView, main, RegisterFormView, loading,register_home

app_name = "msrs"

urlpatterns = [
  path("", main, name="home"),
  # path('form/', views.form, name='form'),
  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
  #path('screening/<int:step>/', FormWizardView.as_view(), name='screening_form'),
  path('screening/', FormWizardView.as_view(), name='screening_form'),
  path('register/<int:step>/', RegisterFormView.as_view(), name='register_form'),
  path("loading/<int:form_data_id>", loading, name='loading_form'),
  path("cadastro/<int:form_data_id>",register_home, name='register_home'),
]

