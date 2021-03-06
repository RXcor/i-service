from django.urls import path

import i_auth.views.jwt

urlpatterns = [
    path('token/login', i_auth.views.jwt.WuiTokenObtainPairView.as_view()),
    path('token/refresh', i_auth.views.jwt.WuiTokenRefreshView.as_view()),
    path('token/logout', i_auth.views.jwt.WuiTokenLogoutView.as_view()),
]
