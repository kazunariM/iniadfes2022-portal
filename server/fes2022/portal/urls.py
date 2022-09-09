from django.urls import path
from . import views


urlpatterns = [
    path('v1/preregistration/', views.PreRegistrationView.as_view(), name="preregistration"),
]
