import urllib.request
from flask import Flask, request
from redis import Redis

redis = Redis.from_url("redis://localhost")

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return """
        <form method="post">
            URL: <input name="url" type="text" /><br />
            <input type="checkbox" name="force" /> Récupérer la page même si elle est dans la cache<br />
            <button type="submit" />Récupérer</button>
        </form>"""

@app.route("/", methods=['POST'])
def show_page():
    url = request.form['url']
    force = request.form.get('force', None)
    cache_key = "page-{0}".format(url)

    if force:
        # en supprimant la clé dans Redis, on s'assure de toujours faire la requête HTTP
        redis.delete(cache_key)

    page = redis.get(cache_key) #si la clé n'existe pas, ça retourne None
    if not page:
        page = fetch_page(url)

    # On met en cache la page récupérée dans Redis avec une expiration de 30 secondes
    redis.set(cache_key, page, ex=30)

    return page

def fetch_page(url):
    with urllib.request.urlopen(url) as f:
        return f.read().decode('utf-8')

