from config import config_manager

class ServiceHealth:
    def get_health(self):
        cfg = config_manager.get_config()
        return {"status": cfg.test.test}
