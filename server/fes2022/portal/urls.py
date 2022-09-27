from django.urls import path

from .views import portal_top, registration


urlpatterns = [
    path('v1/initial/', registration.GetCsrf.as_view(), name="initial"),

    path('v1/registration/', registration.RegistrationView.as_view(), name="api_registration"),
    path('v1/namecards/', registration.NamecardView.as_view(), name="api_namecards"),
    path('v1/complete/<uuid:management_uuid>/', registration.CompleteView.as_view(), name="api_complete"),    

    path('v1/open/<uuid:qrid>/', portal_top.OpenAPI.as_view(), name="api_open"),
    path('v1/portaltop/<uuid:userid>/', portal_top.PortalTopAPI.as_view(), name="api_portal_top"),
]
