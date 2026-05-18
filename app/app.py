from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'DevSecOps Pipeline is Live!',
        'author': 'Your Name',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'production'),
        'timestamp': str(datetime.datetime.utcnow())
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'devsecops-app',
        'timestamp': str(datetime.datetime.utcnow())
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'app': 'DevSecOps Demo Application',
        'environment': os.getenv('ENVIRONMENT', 'production'),
        'version': os.getenv('APP_VERSION', '1.0.0')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)