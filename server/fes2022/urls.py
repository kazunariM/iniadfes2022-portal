from django.urls import path
from .views import QRlistView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('data/qrlist/', login_required(QRlistView.as_view()), name="data_list"),
]
