"""
Модифицированые View из rest_framework_simplejwt для хранения
refresh токена в cookie
"""
import datetime

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt import serializers


__all__ = ('WuiTokenObtainPairSerializer',
           'WuiTokenRefreshSerializer',
           'WuiTokenObtainPairView',
           'WuiTokenRefreshView',
           'WuiTokenLogoutView',)


class WuiRefreshTokenCookieMixin:
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            request.data.pop('refresh', None)
            refresh_token = request.COOKIES.get('refresh')
            request.data['refresh'] = refresh_token
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        remember = serializer.validated_data.get('remember')
        refresh_token = serializer.validated_data.pop('refresh', None)
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        if refresh_token is not None:
            expires = (datetime.datetime.now() + api_settings.REFRESH_TOKEN_LIFETIME) if remember else None
            response.set_cookie(
                'refresh',
                refresh_token,
                expires=expires
            )
        return response


class WuiTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):
    def get_token(self, user):

        token = super().get_token(user)
        token['remember'] = bool(self.initial_data['remember'])
        token['sub'] = str(user.id)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['remember'] = refresh['remember']
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class WuiTokenRefreshSerializer(serializers.TokenRefreshSerializer):
    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token), 'remember': refresh['remember']}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    refresh.blacklist()
                except AttributeError:
                    pass

            refresh.set_jti()
            refresh.set_exp()
            data['refresh'] = str(refresh)
        return data


class WuiTokenObtainPairView(WuiRefreshTokenCookieMixin, TokenObtainPairView):
    serializer_class = WuiTokenObtainPairSerializer


class WuiTokenRefreshView(WuiRefreshTokenCookieMixin, TokenRefreshView):
    serializer_class = WuiTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        if request.COOKIES.get('refresh') is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)


class WuiTokenLogoutView(APIView):
    def get(self, request):
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('refresh')
        return response
