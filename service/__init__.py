from .sev_health import ServiceHealth

# 实例化服务类
service_health = ServiceHealth()

# 导出实例，使外部可以通过 `service.serviceHealth` 访问
__all__ = [
    'service_health'
]