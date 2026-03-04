from flask import Flask, jsonify, render_template, request
from config import STATIONS, TARIFFS  # Your data files
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# HTML PAGES (Keep yours)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find')
def find():
    return render_template('find_station.html')

@app.route('/scheduler')
def scheduler():
    return render_template('scheduler.html')

@app.route('/track')
def track():
    return render_template('track.html')

@app.route('/go_green')
def go_green():
    return render_template('go_green.html')

@app.route('/fast_charge')
def fast_charge():
    return render_template('fast_charge.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

# 🔥 ADD THESE 5 API ROUTES:
@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": "1.0"})

@app.route('/api/stations')
def stations():
    return jsonify(STATIONS)

@app.route('/api/tariffs')
def tariffs():
    return jsonify(TARIFFS)

@app.route('/api/schedule', methods=['POST'])
def schedule():
    data = request.json or {}
    soc = data.get('soc', 20)
    deadline = data.get('deadline', '23:00')
    model = data.get('model', 'Tata Nexon')
    
    # Mock optimal schedule (TNERC tariffs)
    result = {
        "success": True,
        "schedule": [
            {"hour": 22, "kw": 7.2, "cost": 28.80},
            {"hour": 23, "kw": 7.2, "cost": 28.80}
        ],
        "total_cost": 57.60,
        "savings": "50% vs peak"
    }
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
