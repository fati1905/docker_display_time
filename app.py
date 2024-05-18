from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "message": "Hello, World!",
        "current_date": current_date
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)