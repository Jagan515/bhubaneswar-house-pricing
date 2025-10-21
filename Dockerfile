#production reday for render

FROM python:3.11-slim

# Avoid Python output buffering so logs show up instantly
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Copy requirements first (for build caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy everything else — including your app, models, pkl files, etc.
COPY . /app

# Optional: expose for documentation (Render doesn't use this)
EXPOSE 5000

# Start the app using Gunicorn
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:${PORT:-5000} --workers 3"]















# Running it locally via Docker
# # Dockerfile (recommended)
# FROM python:3.11-slim

# # set working directory
# WORKDIR /app

# # copy project files
# COPY . /app

# # upgrade pip & install dependencies
# RUN python -m pip install --upgrade pip \
#  && pip install --no-cache-dir -r requirements.txt

# # expose port (optional)
# EXPOSE 5000

# # run the application
# CMD ["python", "app.py"]
