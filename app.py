from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

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

if __name__ == '__main__':
    app.run(debug=True)
