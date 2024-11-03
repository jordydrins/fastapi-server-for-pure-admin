from config import CFG,CFG_LOG
class ServiceHealth:
    def GetHealth(self):
        CFG_LOG.debug('搞什么啊!!!')
        return {"status": 'GUN'}
