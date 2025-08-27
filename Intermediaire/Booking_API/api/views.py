from .serializers import HotelSerializer, RoomSerializer, ReservationSerializer
from rest_framework import viewsets
from .models import Hotel, Room, Reservation
from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    # @action(detail=True, methods=['get'])
    # def available_rooms(self, request, pk=None):
    #     hotel = self.get_object()
    #     available_rooms = hotel.room_set.filter(reservation__isnull=True)
    #     serializer = self.get_serializer(available_rooms, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')
        check_in = request.data.get('check_in')
        check_out = request.data.get('check_out')
        
        if Reservation.objects.filter(room_id = room_id, check_already_in = check_out, check_already_out = check_in).exists():
            return Response({"Error":"Room unavailable on these dates"})
        
        return super().create(request, *args, **kwargs)