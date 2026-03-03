FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy app files
COPY . .

# Generate logo if needed
RUN python generate_logo.py || true

# Expose port
EXPOSE 5000

# Run with gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
