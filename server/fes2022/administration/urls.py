from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import auth as views_auth
from .views import qr as views_qr
from .views import reception as views_reception


urlpatterns = [
    path('v1/staff/login/', views_auth.SessionView.as_view(), name="staff_login"),
    path('v1/staff/logout/', views_auth.LogoutView.as_view(), name="staff_logout"),
    path('v1/staff/check/', views_auth.CheckUserAPI.as_view(), name="staff_check"),
    path('v1/staff/menu/', views_auth.StaffMenuAPI.as_view(), name="staff_menu"),
    path('v1/staff/pages/<str:page>/', views_auth.PagePermissionAPI.as_view(), name="staff_pages"),

    path('v1/staff/readyroomqr_answer/<int:placeid>/', views_qr.ReadyRoomQRAPI.as_view(), name="staff_readyroomqr_answer"),
    path('v1/staff/roomqr/', views_qr.RoomQRAPI.as_view(), name="staff_roomqr"),

    path('v1/staff/reception/confirmvisitor/<uuid:management_uuid>/', views_reception.ConfirmVisitorAPI.as_view(), name="staff_confirmvisitor"),
    path('v1/staff/reception/selectnamecard/', views_reception.SelectNamecardAPI.as_view(), name="staff_selectnamecard"),
    path('v1/staff/reception/handover/<uuid:management_uuid>/', views_reception.HandedoverAPI.as_view(), name="staff_handover"),
]
