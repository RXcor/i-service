from rest_framework.routers import DefaultRouter

from i_accounts.views import AccountViewSet


router = DefaultRouter()
router.register(r'commands', AccountViewSet, basename='account')

urlpatterns = [
    *router.urls,
]
