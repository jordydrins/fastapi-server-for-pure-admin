# 启动
```
uvicorn main:app --host 0.0.0.0 --port 8585
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8585 main:app
```

```
├── config
│   ├── cfg_logger.py # 对应config.yaml的logger配置
│   ├── cfg_pgsql.py # 对应config.yaml的db配置
│   ├── cfg_test.py # 对应config.yaml的test配置
│   ├── config_core.py  # 核心配置，如 config_name，config_path
│   └── __init__.py #综合其他cfg的config变量类，和单例模式管理 configmanager类，实例化出所有全局对象，例如config，observer，logger，db
├── envconf
│   └── config.yaml
├── initialize
│   ├── int_config.py  # 配置文件监控与加载
│   ├── int_logger.py  # 单例模式管理 日志初始化
│   ├── int_main.py    # 应用初始化
│   ├── int_observer.py  # 单例模式管理 Observer
├── main.py #主入口
├── middleware
│   ├── mid_logger.py #日志中间件
```