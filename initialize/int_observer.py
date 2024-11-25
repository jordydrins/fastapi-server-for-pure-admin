from watchdog.observers import Observer
from config.cfg_core import config_path
import threading

class ObserverManager:
    _instance = None
    _lock = threading.RLock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(ObserverManager, cls).__new__(cls)
                    cls._instance._observer = None
        return cls._instance
        
    def start_observer(self, event_handler, path=config_path):
        with self._lock:
            if self._observer is None:
                self._observer = Observer()
            else:
                print('⚠️  YAML监控服务已经启动，无需重复启动')

            # 检查并启动 Observer，并确保绑定事件处理器
            if not self._observer.is_alive():
                self._observer.schedule(event_handler, path=path, recursive=False)
                self._observer.start()
                print('▶️  YAML监控 启动 成功')
            else:
                print('⚠️  YAML监控线程已经启动，无需重复启动')

    def stop_observer(self):
        with self._lock:
            if self._observer and self._observer.is_alive():
                self._observer.stop()
                self._observer.join()
                self._observer = None
                print("⏹️  YAML监控 停止")
            else:
                print('⚠️  没有可停止的 YAML 监控')


# 创建 ObserverManager 的全局实例
observer_manager = ObserverManager()