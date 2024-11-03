# 启动
```
uvicorn main:app --host 0.0.0.0 --port 8585
gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8585 main:app
```

