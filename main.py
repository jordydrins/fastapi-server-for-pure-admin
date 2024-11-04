from fastapi import FastAPI
from initialize.int_main import create_app,clean_app
from config import conf



app = FastAPI()



@app.on_event("startup")
async def startup_event():
    create_app(app)



@app.on_event("shutdown")
def shutdown_event():
    clean_app(app)


@app.get('/')
async def index_url():
    return {'msg':app.state.config.test}

# 启动应用
# if __name__ == "__main__":
#     print('▶️  ------启动服务------')
#     run(app, host="0.0.0.0", port=8585)
