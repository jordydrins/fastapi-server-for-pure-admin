from time import time,sleep
from watchdog.events import FileSystemEventHandler
from config.cfg_core import config_name
from config import config_manager

class ConfigFileHandler(FileSystemEventHandler):  
    def __init__(self):
        super().__init__()
        self.last_modified_time = 0  # 防止重复触发

    def on_modified(self, event):
        if event.src_path.endswith(config_name):  # 使用后缀筛选
            try:
                sleep(0.1)  # 等待写入完成
                current_time = time()
                if current_time - self.last_modified_time > 1:
                    self.last_modified_time = current_time

                    config_manager.load_config()
                    print("✅ Config 更新 成功")
            except Exception as e:
                print(f"⚠️ Config 更新 失败: {e}")

config_file_handler = ConfigFileHandler()