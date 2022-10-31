from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import HallSerializer
@api_view(['POST'])
def createHall(request):
    hs=HallSerializer(request.data)
    if hs.is_valid():
        hs.save()
    return Response(hs.data)
