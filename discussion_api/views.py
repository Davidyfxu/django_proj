from discussion_api.models import DiscussionData
from rest_framework.decorators import api_view
from rest_framework.response import Response

from discussion_api.serializers import DiscussionSerializer


@api_view(['POST', "OPTIONS"])
def get_all_discussion_data(request):
    print("get_all_discussion_data POST", request.POST)
    print("get_all_discussion_data data", request.data)
    course_id = request.POST.get('course_id') or request.data.get('course_id')
    discussions = DiscussionData.objects.get(course_id=course_id)

    # discussions = DiscussionData.objects.all()
    serializer = DiscussionSerializer(discussions)
    # serializer = DiscussionSerializer(discussions, many=True)
    return Response(serializer.data)
