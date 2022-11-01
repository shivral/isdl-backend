from .models import Booking, User
from rest_framework.decorators import api_view
from .serializers import AdminLoginSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta,datetime
import jwt
from .views import authadmin,Decode
'''admin views '''

@api_view(['POST'])
def registerAdmin(request):
    serializer=AdminLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def loginAdmin(request):
    email=request.data['email']
    password=request.data['password']
    user=User.objects.filter(email=email).first()
    if user==None:
        raise AuthenticationFailed('User not found')
    if user.check_password(password)==False:
        raise AuthenticationFailed("incorrect password")
    payload={
        'id':user.id,  # type: ignore
        'name':user.name,
        'email':user.email,
        'exp':datetime.utcnow()+timedelta(minutes=30),
        'iat':datetime.utcnow()       
    }

    token=jwt.encode(payload=payload,key='secret',algorithm='HS256')
    response=Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    decode=jwt.decode(token,'secret',algorithms=['HS256'])
    response.data={'jwt':token}
    return response

@api_view(['GET'])
def getAllPending(request):
    admin=authadmin(request)
    if admin:
        qs=Booking.objects.filter(pending=True)
        ser=BookingSerializer(list(qs),many=True)
        return Response(ser.data)
    else:
        return AuthenticationFailed("unauthenticated")

    