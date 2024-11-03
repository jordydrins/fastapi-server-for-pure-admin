from fastapi import APIRouter
from api.api_health import router as router_health  # 导入 API 路由

router_api = APIRouter()


router_api.include_router(router_health, prefix="/health", tags=["health"])
