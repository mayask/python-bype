
![](http://i.imgur.com/1caRZYl.png)

# python-bype
bype - Python Fluent DSL

## Example

```python
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
        response = response or dict()

        assert self.status == status

        for key in response:
            assert response[key] == self.response[key]


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
```
