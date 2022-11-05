from .views import authuser,Decode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hall, LectureHall
from .models import Booking,User
from .serializers import BookingSerializer,HallSerializer,UserSerializer
from datetime import datetime
from .email import sendMail
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
        date=request.query_params.get('date',None) #d m y  y m d
        dt=date.strip().split("/")
        d=dt[0]
        m=dt[1]
        y=dt[2]
        date=y+"-"+m+"-"+d
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
def getUser(request):
    id=request.query_params.get('id')
    user=User.objects.get(id=id)
    return Response(UserSerializer(user).data)

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


@api_view(["POST"])
def feedback(request):
    bod=request.data['issue']
    try:
        sendMail(bod,toaddr="shivral312002@gmail.com")
        return Response({"email":"success"})
    except Exception as e:
        print(e)
        return Response({"email":"Failure"})