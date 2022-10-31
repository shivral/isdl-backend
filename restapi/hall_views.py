from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import LectureHall
from .serializers import HallSerializer
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