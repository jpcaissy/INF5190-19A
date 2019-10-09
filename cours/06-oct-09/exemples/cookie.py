import string
import random

from flask import Flask, make_response

app = Flask(__name__)

def random_string():
    choices = string.ascii_letters + string.digits
    return ''.join(random.choice(choices) for i in range(16))

@app.route('/')
def cookie():
    cookie_value = random_string()
    resp = make_response("<h1>Hello World!</h1>")

    resp.set_cookie("session", cookie_value, httponly=True)
    resp.set_cookie("autre_cookie", "bonjour!")
    resp.set_cookie("autre_cookie_secure", "bonjour!", httponly=True, secure=True)

    return resp
