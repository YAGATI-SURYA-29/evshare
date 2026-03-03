# EVShare Frontend

A modern, responsive EV charging platform frontend with animations, map integration, and CO2 tracking.

## 🚀 Features

- **Home Page**: Hero section with animated cards linking to key features
- **Find Station**: Interactive Leaflet map with sample charging stations at Avadi
- **Scheduler**: Book charging sessions and export PDFs
- **Fast Charging Guide**: Best practices for rapid EV charging (CCS, CHAdeMO, Type 2)
- **Go Green**: CO2 savings calculator to track environmental impact
- **Login Page**: Animated login with confetti celebration
- **Responsive Design**: Mobile-first Bootstrap 5 layout
- **Animations**: Fade-in, slide, hover lift, pulse effects

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Flask (Python)
- **Maps**: Leaflet.js with OpenStreetMap
- **PDF Export**: jsPDF CDN
- **Animations**: canvas-confetti, custom CSS keyframes
- **Version Control**: Git & GitHub

## 📋 Setup & Run Locally

### Prerequisites
- Python 3.8+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/YAGATI-SURYA-29/evshare.git
cd evshare

# Switch to frontend branch
git checkout frontend

# Create virtual environment
python -m venv venv

# Activate venv (Windows)
.\venv\Scripts\Activate.ps1

# Or macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate logo (if not already created)
python generate_logo.py

# Start Flask dev server
python app.py
```

Visit: **http://127.0.0.1:5000**

### Access from LAN
Replace `127.0.0.1` with your machine's IP (find via `ipconfig` on Windows or `ifconfig` on Mac/Linux):
```
http://<your-machine-ip>:5000
```

## 📂 Project Structure

```
evshare-frontend/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── generate_logo.py           # Logo generation script
│
├── templates/                 # Jinja2 HTML templates
│   ├── base.html             # Navbar + layout base
│   ├── index.html            # Home (hero + features)
│   ├── find_station.html     # Map with stations
│   ├── scheduler.html        # Booking form
│   ├── fast_charge.html      # Charging guide
│   ├── go_green.html         # CO2 calculator
│   ├── login.html            # Login form
│   ├── signup.html           # Registration form
│   └── track.html            # Charging status
│
├── static/                   # Static assets
│   ├── css/
│   │   └── style.css         # Green theme + animations
│   ├── js/
│   │   ├── enhancements.js   # PDF export, CO2 calc
│   │   ├── confetti.js       # Confetti animations
│   │   └── leaflet.js        # Map initialization
│   └── images/
│       ├── logo.svg          # SVG logo
│       ├── logo.png          # Generated PNG
│       └── icons/            # Map markers (placeholder)
│
└── README.md                 # This file
```

## 🚢 Deployment Options

### Option 1: **GitHub Pages** (Static Only)
For hosting just the HTML/CSS/JS without Flask:

1. Go to repo **Settings** → **Pages**
2. Set **Source** to `frontend` branch, `/root` folder
3. GitHub will deploy to: `https://YAGATI-SURYA-29.github.io/evshare/`

⚠️ **Limitation**: Flask APIs won't work on GitHub Pages. You need a backend server.

### Option 2: **Heroku** (All-in-One)
Deploy both Flask backend + frontend together:

```bash
# Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
heroku login
heroku create your-evshare-app
git push heroku frontend:main
heroku logs --tail
```

**Live URL**: `https://your-evshare-app.herokuapp.com`

### Option 3: **Railway.app** (Simple & Fast)
1. Go to https://railway.app
2. Click **New Project** → **Deploy from GitHub**
3. Connect your GitHub account and select `evshare` repo
4. Railway auto-detects Python, select `frontend` branch
5. Add environment variable `PORT` = `5000`
6. Deploy! (auto-deploys on git push)

**Live URL**: Provided by Railway dashboard

### Option 4: **Render.com** (Recommended)
1. Go to https://render.com/dashboard
2. New → **Web Service**
3. Connect GitHub repo → `evshare`
4. Configure:
   - **Runtime**: Python 3.9
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Deploy

**Live URL**: `https://your-app-name.onrender.com`

### Option 5: **Docker + Any Cloud**

Create `Dockerfile` in repo root:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

Works on AWS, Google Cloud, Azure, DigitalOcean, etc.

## 🔗 Backend Integration

To connect with your backend API in the same repo:

Edit `static/js/enhancements.js`:
```javascript
const API_BASE = 'https://your-deployed-backend.com/api';

// Example: Fetch real stations
async function loadStations() {
  try {
    const res = await fetch(`${API_BASE}/stations`);
    const stations = await res.json();
    // Update Leaflet map with real data
  } catch (e) {
    console.error('Failed to load stations:', e);
  }
}
```

## 🎨 Customization

### Change Brand Color
Edit `static/css/style.css`:
```css
:root {
  --brand: #1fa36c;  /* Change green to your color */
  --accent: #0b5;
}
```

### Update Logo
Replace `static/images/logo.png` with your own 200x100 PNG image.

### Add Your Company Name
Edit `templates/base.html`:
```html
<a class="navbar-brand" href="/">YOUR_COMPANY_NAME</a>
```

## 📱 Available Routes

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Landing page with feature cards |
| Find Station | `/find` | Interactive map (Leaflet) |
| Scheduler | `/scheduler` | Booking form + PDF export |
| Fast Charging | `/fast_charge` | Charging best practices |
| Go Green | `/go_green` | CO2 savings calculator |
| Login | `/login` | User authentication (stub) |
| Signup | `/signup` | User registration (stub) |
| Track | `/track` | Charging status (stub) |

## 🔐 Environment Variables

Create `.env` file (for local dev):
```
FLASK_ENV=development
API_BASE_URL=http://localhost:5000
SECRET_KEY=your-secret-key
```

For production, set these in your hosting platform's dashboard.

## 📦 Dependencies

- `Flask 3.1.3` — Web framework
- `Pillow 12.1.1` — Image generation
- `Jinja2` — Template engine
- `Werkzeug` — WSGI utilities

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Map is empty | Check F12 console for Leaflet JS errors; verify CDN is accessible |
| PDF export fails | Ensure jsPDF CDN is loaded; check browser console |
| Confetti not working | Verify canvas-confetti library is loaded from CDN |
| 404 errors | Make sure Flask is running and routes are defined in `app.py` |
| Port 5000 in use | Change `app.run(port=5001)` in `app.py` |

## 📚 External Libraries (CDN)

- Bootstrap 5: `cdn.jsdelivr.net`
- Leaflet.js: `unpkg.com`
- jsPDF: `cdnjs.cloudflare.com`
- Canvas Confetti: `cdn.jsdelivr.net`

## 🚀 One-Click Deploy to Render

1. Push code: `git push origin frontend`
2. Visit: https://render.com/dashboard
3. Click **New +** → **Web Service**
4. Connect GitHub, select `evshare`, branch `frontend`
5. Build: `pip install -r requirements.txt`
6. Start: `gunicorn app:app`
7. Deploy!

**Your live app**: `https://app-name.onrender.com`

## 📄 License

MIT License — free to use and modify

## 👥 Team

- **Frontend**: @ds806
- **Backend**: @YAGATI-SURYA-29

---

**Questions?** Check the `templates/` and `static/` folders for inline comments, or open an issue on GitHub!
