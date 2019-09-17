import waitress

class LogRequest(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        print("Request for {0}".format(path))
        return self.app(environ, start_response)

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, world!\n']

waitress.serve(LogRequest(app), port=8080)
