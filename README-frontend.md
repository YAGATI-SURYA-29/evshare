EVShare Frontend

Setup notes:
- Uses Bootstrap 5 via CDN in `templates/base.html`.
- Static assets live under `static/` (css, js, images).
- Templates are Jinja-compatible for Flask/Django.
- Leaflet map with sample station markers.
- Client-side PDF export enabled via jsPDF CDN.
- Login form enhanced with animations and confetti (canvas-confetti).

## Running

Create a Python virtual environment and install requirements:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Generate the PNG logo and start server:

```powershell
python generate_logo.py
python app.py
```

By default the Flask dev server listens on `0.0.0.0`, making it reachable from other devices on the same LAN at `http://<your-machine-ip>:5000`.

## Notes

- Replace `static/images/logo.png` with a production-quality image.
- `app.py` currently contains stub routes and does not perform real authentication.
- Map and scheduler pages use placeholder data and logic; extend as needed.
