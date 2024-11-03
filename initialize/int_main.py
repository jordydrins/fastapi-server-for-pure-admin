

from fastapi import FastAPI
from time import sleep
from config import CFG
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from threading import Thread
from sys import exit
from config import Config
from initialize.int_logger import init_logger
from router.rou_health import router_api
from threading import Lock
import hashlib


class ConfigFileHandler(FileSystemEventHandler):  
    def __init__(self):
        super().__init__()  # 确保父类初始化
        self.configName = 'config.yaml'
        self.config = CFG # 使用全局配置实例 
        self.last_hash = None
  
    def file_hash(self, filepath):
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
        
    def on_modified(self, event):
        if event.src_path == f'.\{self.configName}':
            #current_hash = self.file_hash(event.src_path)
            #if current_hash != self.last_hash:
            #    self.last_hash = current_hash
            sleep(0.1)  # 等待文件写入稳定
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


def creat_app(app):
    observer = Observer()
    start_config_watcher(observer)
    # 赋值给全局日志对象
    CFG_LOG = init_logger()
    # 注册路由
    app.include_router(router_api)
    #app.include_router(custom_bp)
    #return app
    app.state.observer = observer

def cleanup(observer):
    observer.stop()
    observer.join()
    print("⏹️  YAML监控已停止")