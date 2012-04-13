from twisted.web import server, resource
from twisted.internet import reactor,protocol,task
import logging
import logging.handlers

log = logging.getLogger('server')
log.setLevel(logging.DEBUG)
shandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
shandler.setFormatter(formatter)
log.addHandler(shandler)

class SongIndex:

    def __call__(self):
        log.info('brack')

    @staticmethod
    def install():
        log.info('activating periodic task')
        t = task.LoopingCall(SongIndex())
        t.start(10.0)

class UI(resource.Resource):
    isLeaf = True
    numberRequests = 0
                
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/html")
        log.info('Request: %s', str(request))
        return "I am request #" + str(self.numberRequests) + "\n"

if __name__ == '__main__':
    log.info('Starting server')
    SongIndex.install()
    reactor.listenTCP(8080, server.Site(UI()))
    reactor.run()
