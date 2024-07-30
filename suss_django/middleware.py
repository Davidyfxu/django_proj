import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


def validate_token(token):
    if token:
        try:
            # 解密并验证 JWT
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print(f"Decoded Token: {decoded_token}")

            # 从解密后的数据中获取 user_id 和 username
            user_id = decoded_token.get('user_id')
            username = decoded_token.get('username')

            if not user_id or not username:
                raise AuthenticationFailed("Invalid token payload")

            # 查找用户
            try:
                user = User.objects.get(id=user_id, username=username)
            except User.DoesNotExist:
                raise AuthenticationFailed("User does not exist")

            # 验证 user_id 和 username 是否匹配
            if user.username != username or user.id != user_id:
                raise AuthenticationFailed("User information does not match")

            # 验证成功
            return user

        except jwt.ExpiredSignatureError:
            print("Token has expired")
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            print("Invalid token")
            raise AuthenticationFailed("Invalid token")


WHITE_API_LIST = ['/api/init/users/login/']


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求前的逻辑
        print("RequestMiddleware: Before view")

        no_auth = request.META.get('PATH_INFO', '') in WHITE_API_LIST

        # 获取请求头部的 Authorization 字段
        auth_header = request.META.get('HTTP_TOKEN', '')
        token = auth_header.split(' ')[-1] if auth_header else None

        print("11111111", token)
        if not no_auth:
            try:
                user = validate_token(token)
                print(f"User validated: {user}")
            except AuthenticationFailed as e:
                print(f"Authentication failed: {str(e)}")

        response = self.get_response(request)

        # 处理响应后的逻辑
        print("RequestMiddleware: After view")

        return response
