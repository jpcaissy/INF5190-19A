def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')]
    # TODO : Afficher un hello world

def hello(environ, start_response):
    pass

routes = [
    #('/hello', hello)
    ('/', hello_world),
]

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for uri, callback in routes:
        if path.startswith(uri):
            return callback(environ, start_response)

    return not_found(environ, start_response)
