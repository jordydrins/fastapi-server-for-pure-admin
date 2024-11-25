from config import config_manager,logger_manager
from .int_config_watcher import config_file_handler
from .int_observer import observer_manager
from router.rou_health import router_api as router_api_health

def init_core():
    # 加载 config
    config_manager.load_config()
    # 初始化 logger
    logger_manager.init_logger(config_manager.get_config().log)

def create_app(app):
    # 启动配置监控
    observer_manager.start_observer(config_file_handler)
    
    # 注册路由
    app.include_router(router_api_health)
    print('✅ Router 注册 成功')

def clean_app():
    observer_manager.stop_observer()
    print("⏹️  资源已全部关闭")