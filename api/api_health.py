from fastapi import APIRouter, Depends
from service import serviceHealth # 引用实例
#from initialize.log import LOG

router = APIRouter()

@router.get('/')
async def get_health(goMsg: str):
    #LOG.info(f"Fetching data for user {user_id}")
    resultData = serviceHealth.get_health()
    return {'code': goMsg,'data':resultData}
