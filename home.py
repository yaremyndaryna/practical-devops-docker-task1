import os
import time
import redis
from flask import Flask

REDIS_ADDRESS = os.getenv('REDIS_ADDRESS')
REDIS_PORT = os.environ.get('REDIS_PORT')

app = Flask(__name__)
cache = redis.Redis(host=REDIS_ADDRESS, port=REDIS_PORT)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello from root'

@app.route('/db')
def db():
    return f'{cache.info("Server")}'

