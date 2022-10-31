from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Hall
from .serializers import HallSerializer
@api_view(['POST'])
def createHall(request):
    hs=HallSerializer(data=request.data)
    if hs.is_valid():
        hs.save()
    qs=Hall.objects.all()
    hsall=HallSerializer(data=qs,many=True)
    return Response(hsall.data)
