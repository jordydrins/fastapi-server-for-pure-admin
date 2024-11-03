import yaml
from loguru import logger
from .cfg_logger import ConfigLogger
from .cfg_pgsql import ConfigDb

# 全局变量
CFG = None
CFG_LOG = logger

class Config:
    def __init__(self, log: ConfigLogger,db: ConfigDb):
        self.log = log
        self.db = db


# 加载 YAML 配置文件
def LoadConfig():
    with open("config.yaml", "r", encoding='utf-8') as f:
        config = yaml.safe_load(f)

    configLog = config['log']
    configDb = config['db']

    return Config(
        log=ConfigLogger(**configLog),
        db=ConfigDb(**configDb)
        )


CFG = LoadConfig()

