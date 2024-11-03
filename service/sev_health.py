from config import CFG,CFG_LOG
class ServiceHealth:
    def get_health(self):
        CFG_LOG.info(CFG.log.format)
        return {"status": CFG}
