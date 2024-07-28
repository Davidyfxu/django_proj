from django.http import HttpResponse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo_api.models import TodoItem
from todo_api.serializers import TodoItemSerializer


def test_connection(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
    return HttpResponse(f"Connected to database: {row[0]}")


@api_view(['GET'])
def get_todos(request):
    todos = TodoItem.objects.all()
    serializer = TodoItemSerializer(todos, many=True)
    return Response(serializer.data)
