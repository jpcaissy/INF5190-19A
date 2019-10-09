from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, {0}!</h1>'.format(request.args.get('name'))
