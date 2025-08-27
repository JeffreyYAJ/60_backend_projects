from rest_framework import serializers
from .views import HotelViewSet, ReservationViewSet, RoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hotels', HotelViewSet)
router.register('rooms', RoomViewSet)
router.register('reservations', ReservationViewSet)

urlpatterns = router.urls


