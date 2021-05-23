from rest_framework.routers import DefaultRouter

from i_job.views import JobViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    *router.urls,
]
