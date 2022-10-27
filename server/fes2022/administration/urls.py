from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import auth as views_auth
from .views import campus as views_campus
from .views import qr as views_qr
from .views import reception as views_reception
from .views import watching as views_watching
from .views import prereg as views_prereg


urlpatterns = [
    path('v1/staff/login/', views_auth.SessionView.as_view(), name="staff_login"),
    path('v1/staff/logout/', views_auth.LogoutView.as_view(), name="staff_logout"),
    path('v1/staff/check/', views_auth.CheckUserAPI.as_view(), name="staff_check"),

    # 管理画面トップ関連
    path('v1/staff/menu/', views_auth.StaffMenuAPI.as_view(), name="staff_menu"),
    path('v1/staff/pages/<str:page>/', views_auth.PagePermissionAPI.as_view(), name="staff_pages"),

    # 入退構のQRリーダー関連
    path('v1/staff/campusqr/enter/', views_campus.EnterCampusAPI.as_view(), name='staff_campusqr_enter'),
    path('v1/staff/campusqr/exit/', views_campus.ExitCampusAPI.as_view(), name='staff_campusqr_exit'),

    # 教室のQRリーダー関連
    path('v1/staff/existplaceid/<int:placeid>/', views_qr.ExistPlaceid.as_view(), name="staff_existplaceid"),
    path('v1/staff/readyroomqr_answer/<int:placeid>/', views_qr.ReadyRoomQRAPI.as_view(), name="staff_readyroomqr_answer"),
    path('v1/staff/roomqr/', views_qr.RoomQRAPI.as_view(), name="staff_roomqr"),
    path('v1/staff/room/<int:placeid>/', views_qr.RoomPeopleAPI.as_view(), name="staff_room"),

    # 受付のネームカード発行関連
    path('v1/staff/reception/confirmvisitor/<uuid:management_uuid>/', views_reception.ConfirmVisitorAPI.as_view(), name="staff_confirmvisitor"),
    path('v1/staff/reception/selectnamecard/', views_reception.SelectNamecardAPI.as_view(), name="staff_selectnamecard"),
    path('v1/staff/reception/handover/<uuid:management_uuid>/', views_reception.HandedoverAPI.as_view(), name="staff_handover"),
    
    # 人数確認
    path('v1/staff/watching/campus/', views_watching.CampusPeopleAPI.as_view(), name='staff_watching_campus'),
    path('v1/staff/watching/room/', views_watching.RoomPeopleAPI.as_view(), name='staff_watching_room'),

    # 事前登録用QR割り当て
    path('v1/staff/allocate/', views_prereg.AllocationQRIDAPI.as_view(), name='staff_allocate'),
    path('v1/staff/get_prereg/not_printing/', views_prereg.PreRegListAPI.as_view(), name='staff_get_prereg_not_printing'),
    path('v1/staff/printed/<uuid:userid>/', views_prereg.PrintedQRAPI.as_view(), name='staff_printed'),
]
