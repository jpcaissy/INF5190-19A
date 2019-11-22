import urllib.request

import click
from flask import Flask, request, redirect, url_for
from redis import Redis
from rq import Queue, Worker

redis = Redis.from_url("redis://localhost")
queue = Queue(connection=redis)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return """<form method="post">URL: <input name="url" type="text" /><button type="submit" />Récupérer</button></form>"""

@app.route("/", methods=['POST'])
def show_page():
    url = request.form['url']

    cache_key = "url-{0}".format(url)

    page = redis.get(cache_key)
    if not page :
        job = queue.enqueue(fetch_page, url)
        return redirect(url_for('verify_job', job_id=job.id))
    else:
        return page

@app.route("/<string:job_id>")
def verify_job(job_id):
    job = queue.fetch_job(job_id)
    if not job.is_finished:
        return "La job n'est toujours pas terminée"

    return job.result

def fetch_page(url):
    with urllib.request.urlopen(url) as f:
        page = f.read().decode('utf-8')

    cache_key = "url-{0}".format(url)
    redis.set(cache_key, page)

    return page

@app.cli.command("worker")
def rq_worker():
    worker = Worker([queue], connection=redis)
    worker.work()
