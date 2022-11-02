from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import LectureHall,Booking
from .serializers import HallSerializer,BookingSerializer
@api_view(['POST'])
def createHall(request):
    hs=HallSerializer(data=request.data)
    if hs.is_valid():
        hs.save()
    else:
        print(LectureHall.objects.all())
    qs=list(LectureHall.objects.all())
    hsall=HallSerializer(qs,many=True)
    return Response(hsall.data)

@api_view(['get'])
def getAllBookings(request):
    bs=BookingSerializer(list(Booking.objects.all()),many=True)
    return Response(bs.data)