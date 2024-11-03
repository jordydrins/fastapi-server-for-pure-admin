from fastapi import APIRouter, Depends
from service import serviceHealth # 引用实例
#from initialize.log import LOG

router = APIRouter()

@router.get('/')
async def GetHealth(goMsg: str):
    #LOG.info(f"Fetching data for user {user_id}")
    resultData = serviceHealth.GetHealth()
    return {'code': goMsg,'data':resultData}
