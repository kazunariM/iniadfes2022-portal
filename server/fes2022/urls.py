from django.urls import path
from .views import QRlistView


urlpatterns = [
    path('data/qrlist/', QRlistView.as_view(), name="data_list"),
]
