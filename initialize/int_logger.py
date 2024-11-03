from loguru import logger
from config import CFG
import os


def InitLogger():
    # 创建 logs 文件夹
    if not os.path.exists("logs"):
        os.makedirs("logs")
    # 配置 logger
    logger.remove()
    logger.add(
        "logs/logfile.log", 
        rotation=CFG.log.rotation, 
        retention=CFG.log.retention, 
        level=CFG.log.level, 
        format=CFG.log.format)
    return logger


