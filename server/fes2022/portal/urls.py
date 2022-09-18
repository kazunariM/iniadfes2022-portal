from django.urls import path
from .views import registration


urlpatterns = [
    path('v1/initial/', registration.GetCsrf.as_view(), name="initial"),

    path('v1/registration/', registration.RegistrationView.as_view(), name="api_registration"),
    path('v1/namecards/', registration.NamecardView.as_view(), name="api_namecards"),
    path('v1/complete/<uuid:management_uuid>/', registration.CompleteView.as_view(), name="api_complete"),    
]
