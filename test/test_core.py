
from bype import Bype


class MyServer(object):
    def __init__(self, host, port=9090):
        self.host = host
        self.port = port
        self.isrunning = False

    def start(self):
        self.isrunning = True

        print 'server started at %s:%d' % (self.host, self.port)

    def _handle_isprime(self, context):
        number = context['number']
        isprime = True

        for i in range(2, number / 2 + 1):
            if (number % i) == 0:
                isprime = True

        return 200, {'isprime': isprime}

    def request(self, url, context=None):
        assert self.isrunning

        context = context or dict()

        status = 404
        response = {
            'code': status,
            'error': 'Page not found'
        }

        if url == '/isprime':
            status, response = self._handle_isprime(context)

        return status, response


class MyWorkflow(Bype):
    def __init__(self, docstring=None):
        self.server = None
        self.status = None
        self.response = {}

    def kick_off_server(self, host, port=9090):
        self.server = MyServer(host, port=port)
        self.server.start()

    def make_request(self, url, context=None):
        print 'requesting %s...' % url

        self.status, self.response = self.server.request(url, context=context)
        print 'got response', self.status, self.response

    def await_response(self, status, response=None):
        print 'assertion', status, response, 'against', self.status, self.response
        assert self.status == status


def test_simple():
    MyWorkflow('''
        Simple request-response workflow
    '''
    ).kick_off_server(
        'localhost',
        port=9090
    ).make_request(
        '/isprime',
        {
            'number': 13
        }
    ).await_response(
        200,
        {
            'isprime': True
        }
    )
