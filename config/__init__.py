import yaml
from .cfg_logger import ConfigLogger
from .cfg_pgsql import ConfigDb
from .cfg_test import ConfigTest

# 全局变量
configName = 'config.yaml'
class Config:
    def __init__(self, log: ConfigLogger,db: ConfigDb,test: ConfigTest):
        self.log = log
        self.db = db
        self.test = test
    
    def load_config(self):
        try:
            with open(configName, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                if config is None:
                    print("❌ 加载的配置为空，请检查 YAML 文件内容")
                
                config_log = config.get('log', {})
                config_db = config.get('db', {})
                config_test = config.get('test', "")

                self.log = ConfigLogger(**config_log)
                self.db = ConfigDb(**config_db)
                self.test = ConfigTest(config_test)

                print("✅ Config 成功加载")
                return self
                
        except FileNotFoundError:
            print("❌ config.yaml 配置文件未找到")
        except yaml.YAMLError as e:
            print("❌ YAML 解析错误:", e)
        except Exception as e:
            print("❌ 加载配置时出现错误:", e)


conf = Config(ConfigLogger,ConfigDb,ConfigTest)
#conf.load_config()


