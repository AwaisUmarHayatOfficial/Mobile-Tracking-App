from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.environ.get("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

@app.route('/set/<key>/<value>')
def set_key(key, value):
    r.set(key, value)
    return jsonify({key: value})

@app.route('/get/<key>')
def get_key(key):
    value = r.get(key)
    return jsonify({key: value.decode() if value else None})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
