from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.middleware.csrf import get_token
from django.contrib.auth import get_user_model, authenticate, login, logout

from ..serializers import auth as serializer_auth

User = get_user_model()


class CheckUserAPI(APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def get(self, request):
        return Response({'is_authenticated' : request.user.is_authenticated})


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

