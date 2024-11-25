class ConfigLogger:
    def __init__(self,path: str, name: str, level: str,rotation:str,retention:str, formats: str):
        self.path = path              # 日志目录
        self.name = name              # 日志名
        self.level = level            # 指定日志的级别，如 DEBUG, INFO, WARNING, ERROR, CRITICAL 等。
        self.rotation = rotation      # 日志文件的轮转策略，可以指定时间（如 "1 day"）、文件大小（如 10 MB）等。当达到指定条件时，Loguru 会创建新文件。
        self.retention = retention    # 设置日志文件的保留策略，指定多久后自动删除旧的日志文件。例如，"7 days" 或 "10 MB"。不删除用None
        self.formats = formats

    def __repr__(self):
        return f"<日志配置信息(level={self.level},rotation={self.rotation}, retention={self.retention}, formats={self.formats})>"
        # 打印类的实例化对象会打印这里面的内容
