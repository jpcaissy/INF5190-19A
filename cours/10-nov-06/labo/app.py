import pg8000
import redis

from flask import Flask
import click

app = Flask(__name__)

db_conn = pg8000.connect(database="labo_06", user="labo", password="password", host='127.0.0.1', port=5432)
redis_conn = redis.Redis(host='127.0.0.1', port=6379, db=0)

@app.cli.command("init-db")
def init_db():
    cursor = db_conn.cursor()
    cursor.execute("CREATE TABLE visite (id SERIAL, datetime TIMESTAMP)")
    db_conn.commit()

@app.route('/')
def hello_world():
    cursor = db_conn.cursor()

    cursor.execute("SELECT datetime FROM visite ORDER BY id DESC LIMIT 1")
    derniere_visite = cursor.fetchone()[0]

    cursor.execute("INSERT INTO visite (datetime) VALUES (now())")
    db_conn.commit()

    nombre_visites = redis_conn.incr("nombre_visites")

    return f"""Hello, World!<br />
    Ceci est la {nombre_visites}e visite(s).<br />
    La dernière visite était le {derniere_visite}
    """
