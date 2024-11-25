from fastapi import FastAPI
from initialize import init_core,create_app,clean_app
from fastapi.middleware.cors import CORSMiddleware
from middleware.mid_logger import RequestLoggerMiddleware
from config import logger_manager

app = FastAPI()

# 加载config，注册logger
init_core()

# 设置允许的 CORS 来源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，或者指定特定的域
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)
# 注册日志记录中间件
app.add_middleware(RequestLoggerMiddleware,logger = logger_manager.get_logger())

@app.on_event("startup")
async def startup_event():
    create_app(app)

@app.on_event("shutdown")
def shutdown_event():
    clean_app()
