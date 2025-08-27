from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()

router.register('job', JobViewSet)

urlpatterns = router.urls
