from threading import Thread
from watchdog.observers import Observer

from config import conf
from .int_config import ConfigFileHandler
from initialize.int_logger import init_logger
from router.rou_health import router_api



def start_config_watcher(config_name,app):
    event_handler = ConfigFileHandler(config_name,app)
    app.state.observer.schedule(event_handler, path='.', recursive=False)
    observer_thread = Thread(target=app.state.observer.start)
    observer_thread.daemon = True
    observer_thread.start()
    print('▶️  YAML监控启动')


def create_app(app):
    app.state.config_name = './config.yaml'
    app.state.observer = Observer()

    # 注册yaml
    app.state.config = conf.load_config()
    # 注册logger
    app.state.logger = init_logger(app.state.config)

    # 开启yaml监控
    start_config_watcher(app.state.config_name,app)

    # 注册路由
    app.include_router(router_api)
    print('✅ Router 注册完成')

def clean_app(app):
    if hasattr(app.state, "observer"):
        app.state.observer.stop()
        app.state.observer.join()
        print("⏹️  YAML监控停止")

    if hasattr(app.state, "db"):
        app.state.db.close()
        print("⏹️ 数据库连接关闭")

    if hasattr(app.state, "redis"):
        app.state.redis.close()
        print("⏹️ Redis 连接关闭")
    print("⏹️  资源已全部关闭")