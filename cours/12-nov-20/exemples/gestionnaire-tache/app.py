import urllib.request
import urllib.parse

import click
from flask import Flask, request, redirect, url_for
from redis import Redis
from rq import Queue, Worker

redis = Redis(host='127.0.0.1', port=6379, db=0)
task_manager = Queue(connection=redis)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return """<form method="post">URL: <input name="url" type="text" /><button type="submit" />Récupérer</button></form>"""

@app.route("/", methods=['POST'])
def fetch():
    url_to_fetch = request.form['url']
    job = task_manager.enqueue(fetch_url, url_to_fetch)

    return redirect(url_for('view_url', job_id=job.id))

@app.route("/url/<string:job_id>", methods=['GET'])
def view_url(job_id):
    job = task_manager.fetch_job(job_id)
    if job.result:
        return job.result

    else:
        return "Page non récupérée"

def fetch_url(url):
    with urllib.request.urlopen('http://www.python.org/') as f:
        return f.read().decode('utf-8')

@app.cli.command("worker")
def rq_worker():
    worker = Worker([task_manager], connection=redis)
    worker.work()
