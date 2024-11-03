from fastapi import FastAPI
from initialize.int_logger import InitLogger
from config import CFG,CFG_LOG
from router.rou_health import router_api

app = FastAPI()


# 赋值给全局日志对象
CFG_LOG = InitLogger()
# 注册路由
app.include_router(router_api)


# 启动应用
if __name__ == "__main__":
    import uvicorn
    CFG_LOG.info("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8585)
