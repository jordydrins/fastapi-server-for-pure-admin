from fastapi import FastAPI
from initialize.int_main import cleanup,creat_app


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    creat_app(app)
    
    

@app.on_event("shutdown")
def shutdown_event():
    observer = app.state.observer
    cleanup(observer)


# 启动应用
# if __name__ == "__main__":
#     print('▶️  ------启动服务------')
#     run(app, host="0.0.0.0", port=8585)
