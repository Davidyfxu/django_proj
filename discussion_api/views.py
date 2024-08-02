from discussion_api.models import DiscussionData
from rest_framework.decorators import api_view
from rest_framework.response import Response

from discussion_api.serializers import DiscussionSerializer


@api_view(['POST'])
def get_all_discussion_data(request):
    course_id = request.POST.get('course_id')
    discussions = DiscussionData.objects.get(course_id=course_id)

    # discussions = DiscussionData.objects.all()
    serializer = DiscussionSerializer(discussions)
    # serializer = DiscussionSerializer(discussions, many=True)
    return Response(serializer.data)
