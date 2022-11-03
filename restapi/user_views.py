from .views import authuser,Decode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hall, LectureHall
from .models import Booking
from .serializers import BookingSerializer,HallSerializer
from datetime import datetime
#commit
@api_view(['POST','GET'])
def createBooking(request):
    user=authuser(request)
    if user:
        hallid = request.query_params.get('id',None)
        # print("hall id is ",hallid)   s    
        hall = LectureHall.objects.get(id=hallid)
        start=request.query_params.get('start',None)
        end=request.query_params.get('end',None)
        date=request.query_params.get('date',None)
        # nw=datetime.datetime.now()
        # strin=f'{nw.hour}:{nw.minute}:{}'
        ss="2022-11-01T11:01"
        print(start,end)

        Booking.objects.create(user=user,hall=hall,booked=False,pending=True,slotStart=date+" "+start,slotEnd=date+" "+end)                      # type: ignore
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
        qq=Booking.objects.filter(user=user)
        # for hall in user.bookings.all():
            # allBookingsqs=list(Booking.objects.filter(user=user,hall=hall))
            # qs+=allBookingsqs
        return Response(BookingSerializer(qq,many=True).data)
    else:
        return Response({"bad":"no auth"})
