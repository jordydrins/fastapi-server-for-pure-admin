
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

# 记录请求信息与处理时间
class RequestLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, logger):
        super().__init__(app)
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # 缓存请求体，确保它可以被后续操作使用
        request_content = {}
        if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            try:
                # 获取请求体并缓存，防止后续无法读取
                request_content = await request.json()
                # 将请求体存储在 request.state 中，以便后续访问
                request.state.body = request_content
            except Exception:
                # 如果无法解析为 JSON，则读取原始请求体（二进制）
                request_content = await request.body()
                request.state.body = request_content

        elif request.method == "GET":
            request_content = dict(request.query_params)
            request.state.body = request_content  # 对于 GET 请求，使用查询参数作为请求体

        try:
            response = await call_next(request)  # 调用下一个处理器
        except Exception as e:
            self.logger.error(f'{{"method": "{request.method}", "url": "{request.url}","msg":"request 处理错误",  "error": "{str(e)}"}}')
            raise
        
        process_time = time.time() - start_time

        client_ip = request.client.host
        user_agent = request.headers.get("User-Agent", "Unknown")

        # 缓存响应体内容
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk
        response.body_iterator = self._repeat_body(response_body)

        self.logger.info(
            f'{{"method": "{request.method}", "status_code": {response.status_code}, "url": "{request.url}", '
            f'"process_time": "{process_time:.4f}", "client_ip": "{client_ip}","request":"{request_content}","response":"{response_body}"}}'
        ) # , "user_agent": "{user_agent}"

        return response
        
    async def _repeat_body(self, body):
        # 用于重置响应体，以便再次读取
        yield body
