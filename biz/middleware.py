import time
from .models import RequestLog

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        # 记录到数据库或日志
        RequestLog.objects.create(
            path=request.path,
            duration=duration,
            method=request.method
        )
        return response