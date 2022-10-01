from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication
from django.contrib.auth import get_user_model, authenticate, login, logout

from ..models import PagesPermission
from ..serializers import auth as serializer_auth

User = get_user_model()


class CheckUserAPI(APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def get(self, request):
        return Response({'is_authenticated' : request.user.is_authenticated})


class StaffMenuAPI(ListAPIView):
    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = serializer_auth.PagesSerializer

    def get_queryset(self):
        return PagesPermission.objects.all() if self.request.user.is_superuser else self.request.user.pages.all()

    def test_func(self):
        return self.request.user.is_authenticated


class SessionView(APIView):
    serializer_class = serializer_auth.UserSerializer

    def post(self, request):
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user:
            login(request, user)
            return Response({})
        else:
            raise AuthenticationFailed('アカウントが見つかりませんでした')


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response({})


class PagePermissionAPI(APIView):
    def get(self, request, page):
        if request.user.is_superuser:
            return Response({'result' : True})
        elif request.user.is_authenticated:
            return Response({'result' : request.user in PagesPermission.objects.get(page=page).users.all()})
        else:
            return Response({}, status=403)