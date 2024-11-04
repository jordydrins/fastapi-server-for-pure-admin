

from fastapi import FastAPI
from time import sleep,time
from config import CFG
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from threading import Thread
from config import Config
from initialize.int_logger import init_logger
from router.rou_health import router_api



class ConfigFileHandler(FileSystemEventHandler):  
    def __init__(self):
        super().__init__()  # 确保父类初始化
        self.configName = './config.yaml'
        self.config = CFG # 使用全局配置实例 
        self.last_modified_time = 0  # 上次修改时间(因为文件系统保存会触发2次，所以设定间隔，1秒内只更新1次)
  
    def on_modified(self, event):
        if event.src_path == f'{self.configName}':
            sleep(0.1)  # 等待文件写入稳定
            current_time = time()
            # 检查文件是否在1秒内被修改
            if current_time - self.last_modified_time > 1:
                self.last_modified_time = current_time
                print('▶️  Config 发生变化，开始重载')
                self.config.load_config()
                
        else:
            pass
            #print(f'⏸️  检测到文件修改，但是文件名不对，检测到的是:{event.src_path}')



def start_config_watcher(observer):
    event_handler = ConfigFileHandler()
    observer.schedule(event_handler, path='.', recursive=False)
    observer_thread = Thread(target=observer.start)
    observer_thread.daemon = True
    observer_thread.start()
    print('▶️  YAML监控启动')


def creat_app(app):
    observer = Observer()
    start_config_watcher(observer)
    # 赋值给全局日志对象
    CFG_LOG = init_logger()
    # 注册路由
    app.include_router(router_api)
    print('✅ Router 注册完成')
    #app.include_router(custom_bp)
    #return app
    app.state.observer = observer

def cleanup(observer):
    observer.stop()
    observer.join()
    print("⏹️  YAML监控停止")