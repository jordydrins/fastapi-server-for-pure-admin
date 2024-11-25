from fastapi import APIRouter, Depends
from service import service_health # 引用实例
#from initialize.log import LOG

router = APIRouter()

@router.get('/')
async def get_health(go: str):
    result_data = service_health.get_health()
    return {'code': 1,'data':result_data}
