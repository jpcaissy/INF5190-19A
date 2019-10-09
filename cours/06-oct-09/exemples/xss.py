from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Hello, {0}!</h1>'.format(request.args.get('name')))
    response.set_cookie('session', 'cookie_value')

    return response
