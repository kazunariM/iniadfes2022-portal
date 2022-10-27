from django.urls import path

from .views import portal_top, registration, state, stamprally


urlpatterns = [
    path('v1/initial/', registration.GetCsrf.as_view(), name="initial"),

    path('v1/registration/', registration.RegistrationView.as_view(), name="api_registration"),
    path('v1/namecards/', registration.NamecardView.as_view(), name="api_namecards"),
    path('v1/complete/<uuid:management_uuid>/', registration.CompleteView.as_view(), name="api_complete"),    

    path('v1/open/<uuid:qrid>/', portal_top.OpenAPI.as_view(), name="api_open"),
    path('v1/portaltop/<uuid:userid>/', portal_top.PortalTopAPI.as_view(), name="api_portal_top"),
    
    path('v1/state/', state.State.as_view(), name="api_state"),

    path('v1/stamprally/', stamprally.StamprallyList.as_view(), name="api_stamprally"),
    path('v1/stampsheet/<uuid:stampcourse>/', stamprally.StampSheetAPI.as_view(), name="api_stamp_sheet"),
    path('v1/stamps/<uuid:stampcourse>/', stamprally.AllStampAPI.as_view(), name="api_all_stamp"),
    path('v1/stamprally/<uuid:userid>/<uuid:stampcourse>/', stamprally.StampHistroyAPI.as_view(), name="api_got_stamp"),
]
