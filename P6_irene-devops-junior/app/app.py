from flask import Flask, jsonify
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "app": "Irene DevOps Demo",
        "status": "running",
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/health')
def health():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    
    return jsonify({
        "status": "healthy" if cpu < 90 and memory < 90 else "warning",
        "cpu_percent": cpu,
        "memory_percent": memory
    })

@app.route('/metrics')
def metrics():
    return jsonify({
        "requests_served": 100,  # Esto sería dinámico en producción
        "uptime_seconds": 3600
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
