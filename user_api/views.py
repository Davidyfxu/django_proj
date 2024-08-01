from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from utils.index import validate_token
from .serializers import UserSerializer, LoginSerializer


@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token_data = serializer.save()
        return Response(token_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_init(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    token = auth_header.split(' ')[-1] if auth_header else None
    user = validate_token(token)
    if user:
        return Response({"username": user.username, "email": user.email, 'password': user.password},
                        status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
