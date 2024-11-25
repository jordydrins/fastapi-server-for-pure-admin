import threading
from config.cfg_config import Config
from config.cfg_logger import ConfigLogger
from config.cfg_pgsql import ConfigDb
from config.cfg_test import ConfigTest

class ConfigManager:
    _instance = None
    _lock = threading.RLock()
    
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ConfigManager, cls).__new__(cls)
                    cls._instance._config = Config(ConfigLogger,ConfigDb,ConfigTest)  # 初始化配置实例
        return cls._instance

    def load_config(self):
        with self._lock:
            self._config = self._config.load_config()

    def get_config(self):
        return self._config





# 使用单例配置管理器
config_manager = ConfigManager()
