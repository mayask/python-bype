
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

## License

The MIT License (MIT)

Copyright (c) 2015 Maxim Yaskevich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
