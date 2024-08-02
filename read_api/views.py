from rest_framework.decorators import api_view
from rest_framework.response import Response

from read_api.models import ReadData
from read_api.serializers import ReadSerializer


@api_view(['POST'])
def get_all_read_data(request):
    discussions = ReadData.objects.all()
    serializer = ReadSerializer(discussions, many=True)
    return Response(serializer.data)
