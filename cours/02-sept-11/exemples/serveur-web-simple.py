"""

Application web Python communicant avec le protocole HTTP

Utilisation::
    python3 server-web-simple [port=8080]

Pour envoyer une requête :
    curl http://localhost:8080

Pour envoyer une requête POST :
    curl -d "toto=tata&cours=inf5190" http://localhost:8080
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv

class HandlerHTTP(BaseHTTPRequestHandler):
    def set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        self.set_headers()
        self.wfile.write(b"<html><body><h1>Hello World!</h1></body></html>")

    def do_POST(self):
        self.set_headers()
        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")

def run(port):
    httpd = HTTPServer(('localhost', port), HandlerHTTP)

    print("Démarage du serveur HTTP sur le port {0} (http://localhost:{1})".format(port, port))
    httpd.serve_forever()

port = 8080
if len(argv) == 2:
    port = int(argv[1])

run(port)
