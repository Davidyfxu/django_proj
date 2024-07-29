class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求前的逻辑
        print("RequestMiddleware: Before view")

        # 添加自定义请求逻辑，例如在请求头中添加自定义头
        request.META['HTTP_X_CUSTOM_HEADER'] = 'CustomHeaderValue'

        response = self.get_response(request)

        # 处理响应后的逻辑
        print("RequestMiddleware: After view")

        return response
