from time import sleep,time
from watchdog.events import FileSystemEventHandler

from config import conf
from .int_logger import init_logger

class ConfigFileHandler(FileSystemEventHandler):  
    def __init__(self,config_name,app):
        super().__init__()  # 确保父类初始化
        self.config_name = config_name
        self.last_modified_time = 0  # 上次修改时间(因为文件系统保存会触发2次，所以设定间隔，1秒内只更新1次)
        self.app = app
  
    def on_modified(self, event):
        if event.src_path == f'{self.config_name}':
            sleep(0.1)  # 等待文件写入稳定
            current_time = time()
            # 检查文件是否在1秒内被修改
            if current_time - self.last_modified_time > 1:
                self.last_modified_time = current_time
                print('▶️  Config 发生变化，开始重载')
                self.app.state.config = conf.load_config()
                self.app.state.logger = init_logger(self.app.state.config)
                
        else:
            pass
            #print(f'⏸️  检测到文件修改，但是文件名不对，检测到的是:{event.src_path}')