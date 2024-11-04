from fastapi import APIRouter, Depends
from service import service_health # 引用实例
#from initialize.log import LOG

router = APIRouter()

@router.get('/')
async def get_health(goMsg: str):
    #LOG.info(f"Fetching data for user {user_id}")
    #print(app.state.config.db.url)
    result_data = service_health.get_health()
    return {'code': goMsg,'data':result_data}
