from django.urls import path
from .views import auth as views_auth


urlpatterns = [
    path('v1/staff/login/', views_auth.SessionView.as_view(), name="staff_login"),
    path('v1/staff/logout/', views_auth.LogoutView.as_view(), name="staff_logout"),
    path('v1/staff/check/', views_auth.CheckUserAPI.as_view(), name="staff_check"),
]
