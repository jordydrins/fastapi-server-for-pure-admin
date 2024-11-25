from loguru import logger
from os.path import exists
from os import makedirs
import threading


class LoggerManager:
    _instance = None
    _lock = threading.RLock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(LoggerManager, cls).__new__(cls)
                    cls._instance._logger = None
        return cls._instance

    def init_logger(self, log_config):
        # 初始化日志配置
        if not self._logger:
            if not exists(log_config.path):
                makedirs(log_config.path)
            
            # 配置 loguru
            logger.remove()  # 移除默认的 logger
            logger.add(
                f"{log_config.path}/{log_config.name}.info.log",
                rotation=log_config.rotation,
                retention=log_config.retention,
                level='INFO', #log_config.level,
                format=log_config.formats,
                enqueue=True,  # 异步写入日志
                #serialize=True, # 序列化json
                filter=lambda record: record["level"].name == "INFO"
            )
            logger.add(
                f"{log_config.path}/{log_config.name}.error.log",
                rotation=log_config.rotation,
                retention=log_config.retention,
                level='ERROR', #log_config.level,
                format=log_config.formats,
                enqueue=True,  # 异步写入日志
                #serialize=True, # 序列化json
                filter=lambda record: record["level"].name == "ERROR"
            )
            self._logger = logger
            print("✅ Logger 初始化 成功")

    def get_logger(self):
        if not self._logger:
            raise ValueError("❌  Logger 未初始化，请先init！")
        return self._logger

# 实例化一个全局 LoggerManager
logger_manager = LoggerManager()
