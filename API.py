from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize the limiter with default key function (IP address)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]  # Global rate limit
)

@app.route('/')
@limiter.limit("10 per minute")  # Custom rate limit for this route
def home():
    return jsonify({"message": "Welcome to the API Gateway!"})

@app.route('/data')
def data():
    return jsonify({"data": "Here is your data."})

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="Rate limit exceeded. Try again later."), 429

if __name__ == '__main__':
    app.run(debug=True)

