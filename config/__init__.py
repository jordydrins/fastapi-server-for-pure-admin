import yaml
from loguru import logger
from .cfg_logger import ConfigLogger
from .cfg_pgsql import ConfigDb

# 全局变量
configName = 'config.yaml'
CFG = None
CFG_LOG = logger

class Config:
    def __init__(self, log: ConfigLogger,db: ConfigDb):
        self.log = log
        self.db = db
    
    def load_config(self):
        print('重载')
        try:
            with open(configName, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                if config is None:
                    print("❌ 加载的配置为空，请检查 YAML 文件内容")
                
                configLog = config.get('log', {})
                configDb = config.get('db', {})

                self.log = ConfigLogger(**configLog)
                self.db = ConfigDb(**configDb)

                global CFG
                CFG = self
                print("✅ Config 成功加载")
                
        except FileNotFoundError:
            print("❌ config.yaml 配置文件未找到")
        except yaml.YAMLError as e:
            print("❌ YAML 解析错误:", e)
        except Exception as e:
            print("❌ 加载配置时出现错误:", e)


conf = Config(ConfigLogger,ConfigDb)
conf.load_config()


