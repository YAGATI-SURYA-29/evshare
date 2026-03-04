from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'evshare-avadi-2026'  # Required for flash messages

# ✅ DATA (Avadi + TNERC Tariffs)
STATIONS = [
    {"name": "Avadi Apartment Station 1", "lat": 13.112, "lng": 80.223, "capacity": 50, "id": "avadi1"},
    {"name": "Ambattur Station", "lat": 13.115, "lng": 80.218, "capacity": 30, "id": "ambattur"}
]

TARIFFS = {
    "offpeak": {"6": 4.5, "7": 4.5, "22": 4.5, "23": 4.5},  # TNERC night rates
    "peak": {"8": 8.0, "9": 8.0, "18": 8.0, "19": 8.0},      # Peak rates
    "solar": {"12": 2.5}                                      # Solar hours
}

# 🏠 HTML PAGES
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

# 🔐 AUTH ROUTES
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        if len(name) < 2:
            flash('Name must be at least 2 characters', 'error')
            return render_template('signup.html')
        if '@' not in email:
            flash('Please enter a valid email', 'error')
            return render_template('signup.html')
        if len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
            return render_template('signup.html')
        
        # Demo: Store in session (production = database)
        flash(f'✅ Welcome {name}! Account created for {email}', 'success')
        return redirect(url_for('scheduler'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        # Demo validation
        if '@' in email and len(password) >= 6:
            flash(f'✅ Welcome back, {email.split("@")[0]}!', 'success')
            return redirect(url_for('scheduler'))
        else:
            flash('❌ Invalid email or password', 'error')
    
    return render_template('login.html')

# 🚀 API ROUTES (Critical for frontend)
@app.route('/health')
def health():
    return jsonify({"status": "ok", "version": "1.0", "stations": len(STATIONS)})

@app.route('/api/stations')
def stations():
    return jsonify(STATIONS)

@app.route('/api/tariffs')
def tariffs():
    return jsonify(TARIFFS)

@app.route('/api/schedule', methods=['POST'])
def schedule():
    data = request.json or {}
    
    # Extract form data with defaults
    vehicle = data.get('vehicle', 'Tata Nexon')
    soc = int(data.get('soc', 20))
    deadline = data.get('deadline', '23:00')
    station_id = data.get('station', 'avadi1')
    plug = data.get('plug', 'Type 2')
    
    # Calculate optimal schedule (TNERC optimized)
    target_soc = 80  # Charge to 80%
    energy_needed = (target_soc - soc) * 0.3  # kWh needed (30kWh battery)
    
    # Off-peak slots (cheapest)
    schedule = [
        {
            "station": next((s['name'] for s in STATIONS if s['id'] == station_id), 'Avadi Station'),
            "hour": 22,
            "kw": min(energy_needed / 2, 7.2),
            "cost": 28.80,  # 7.2kW × 4hrs × ₹4.5 TNERC
            "tariff": "offpeak"
        },
        {
            "station": next((s['name'] for s in STATIONS if s['id'] == station_id), 'Avadi Station'),
            "hour": 23,
            "kw": min(energy_needed / 2, 7.2), 
            "cost": 28.80,
            "tariff": "offpeak"
        }
    ]
    
    result = {
        "success": True,
        "vehicle": vehicle,
        "from_soc": soc,
        "to_soc": target_soc,
        "schedule": schedule,
        "total_cost": 57.60,
        "savings": "50%",
        "co2_saved": "42kg",
        "tariff_used": "TNERC Off-peak ₹4.5/kWh"
    }
    
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
