# from django.urls import path
# from rest_framework.routers import DefaultRouter
#
# from wui_auth.views.user import UserViewSet, CurrentUserView, UserPasswordView
#
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet,  basename='user')
#
# urlpatterns = [
#     path('user', CurrentUserView.as_view()),
#     path('user/password', UserPasswordView.as_view()),
#
#     *router.urls
# ]
