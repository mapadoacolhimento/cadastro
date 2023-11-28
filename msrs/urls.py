from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    FormWizardView,
    main,
    RegisterFormView,
    loading,
    register_home,
    denail,
)

from .utils import get_cities_for_state

app_name = "msrs"


urlpatterns = [
    path("", main, name="home"),
    # path('form/', views.form, name='form'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('screening/<int:step>/', FormWizardView.as_view(), name='screening_form'),
    path("screening/", FormWizardView.as_view(), name="screening_form"),
    path("register/<int:step>/", RegisterFormView.as_view(), name="register_form"),
    path("denail/<str:type>/", denail, name="denail"),
    path("cadastro/<int:form_data_id>", register_home, name="register_home"),
    path("get_cities_for_state/", get_cities_for_state, name="get_cities_for_state"),
]
