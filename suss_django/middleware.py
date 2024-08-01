from rest_framework.exceptions import AuthenticationFailed

from utils.index import validate_token


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求前的逻辑
        print("RequestMiddleware: Before view")

        no_auth = 'no_auth' in request.META.get('PATH_INFO', '')
        # 获取请求头部的 Authorization 字段
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        token = auth_header.split(' ')[-1] if auth_header else None

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
