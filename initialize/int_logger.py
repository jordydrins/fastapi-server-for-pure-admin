from loguru import logger
from os.path import exists
from os import makedirs


def init_logger(config):
    # 创建 logs 文件夹
    if not exists("logs"):
        makedirs("logs")
    # 配置 logger
    logger.remove()
    logger.add(
        "logs/api.log", 
        rotation=config.log.rotation, 
        retention=config.log.retention, 
        level=config.log.level, 
        format=config.log.format)
    return logger


