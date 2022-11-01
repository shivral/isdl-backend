from .views import authuser,Decode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hall, LectureHall
from .models import Booking
from .serializers import BookingSerializer,HallSerializer
import datetime

@api_view(['POST','GET'])
def createBooking(request):
    user=authuser(request)
    if user:
        hallid = request.query_params.get('id',None)
        # print("hall id is ",hallid)   s    
        hall = LectureHall.objects.get(id=hallid)
        Booking.objects.create(user=user,hall=hall,booked=False,pending=True,slotStart=str(datetime.datetime.now()),slotEnd=str(datetime.datetime.now()))                      # type: ignore
        print(Booking.objects.all())
        hs=HallSerializer(hall)
        return Response(hs.data)
    else:
        return Response({'Data':'Failed'})

@api_view(['GET'])
def getUserBooking(request):
    user=authuser(request)
    if user:
        qs=[]
        for hall in user.bookings.all():
            allBookingsqs=list(Booking.objects.filter(user=user,hall=hall))
            qs+=allBookingsqs
        return Response(BookingSerializer(qs,many=True).data)
    else:
        return Response({"bad":"no auth"})
