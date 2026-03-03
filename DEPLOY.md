# Quick Deployment Guide

## 🚀 Deploy in 5 Minutes

### **Render.com** (Easiest - Recommended)

1. **Create Account**: https://render.com
2. **New Web Service**: 
   - GitHub Repo: `evshare`
   - Branch: `frontend`
   - Runtime: Python 3.9
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
3. **Deploy** → Live in 2-3 minutes
4. **URL**: `https://your-app-name.onrender.com`

---

### **Heroku** (Classic)

```bash
# 1. Install Heroku CLI
# Windows: Download from heroku.com/downloads
# Mac: brew tap heroku/brew && brew install heroku

# 2. Login
heroku login

# 3. Create app
heroku create your-evshare-app

# 4. Deploy
git push heroku frontend:main

# 5. View logs
heroku logs --tail
```

**Live URL**: `https://your-evshare-app.herokuapp.com`

---

### **Railway.app** (Fast)

1. Go to https://railway.app
2. **New Project** → **Deploy from GitHub Repo**
3. Select `evshare` repo, branch `frontend`
4. Railway auto-detects Python
5. Click **Deploy**
6. Get your live URL from dashboard

---

### **Docker + Any Cloud** (AWS, Azure, GCP, DigitalOcean)

```bash
# Build image
docker build -t evshare-frontend .

# Run locally
docker run -p 5000:5000 evshare-frontend

# Push to Docker Hub (for cloud deployment)
docker tag evshare-frontend YOUR_USERNAME/evshare-frontend
docker push YOUR_USERNAME/evshare-frontend

# Deploy to cloud platforms via their container services
```

---

### **GitHub Pages** (Static Only - No Backend)

⚠️ **Limitation**: Only static files (no Flask)

1. Repo → Settings → Pages
2. Source: `frontend` branch
3. Folder: `/root`
4. Save → Auto-deploys to `https://YAGATI-SURYA-29.github.io/evshare/`

---

## 📊 Comparison

| Platform | Cost | Setup Time | Notes |
|----------|------|-----------|-------|
| **Render** | Free | 5 min | Easiest, auto-deploys |
| **Heroku** | Free tier ended | 10 min | Classic choice, reliable |
| **Railway** | Free | 5 min | Modern, fast |
| **GitHub Pages** | Free | 2 min | Static only (no APIs) |
| **Docker** | Varies | 15 min | Most flexible |

---

## 🔧 Environment Variables

Add these in your hosting dashboard:

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
API_BASE_URL=https://your-backend-api.com
```

---

## ✅ Verify Deployment

After deploying, test these routes:

- `https://your-app.com/` — Home page
- `https://your-app.com/find` — Map page
- `https://your-app.com/fast_charge` — Charging guide
- `https://your-app.com/go_green` — CO2 calculator

If all load → **Deployment successful!** 🎉

---

## 🔗 Future: Connect to Backend

Once your backend is deployed, update `static/js/enhancements.js`:

```javascript
const API_BASE = 'https://your-backend-url.com/api';
```

Redeploy → Frontend will fetch real data from backend.

---

**Need help?** Check platform docs or open an issue!
