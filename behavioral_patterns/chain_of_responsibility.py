"""
in order to decouple a request and its processing
processing a request will start by handler, and if a handler
can't process- it has a link to another handler (successor)
that will try to process
"""


class Handler:
    """abstract handler"""

    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('must provide implementation in successor')


class ConcreteHandler(Handler):
    def _handle(self, request):
        if 0 <request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True

class DefaultHandler(Handler):

    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True

class Client:
    def __init__(self):
        self.handler = ConcreteHandler(DefaultHandler(None))

    def delegate(self,requests):
        for request in requests:
            self.handler.handle(request)

c = Client()
requests = [5*i for i in range(4)]

c.delegate(requests)