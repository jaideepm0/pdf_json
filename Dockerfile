# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

# System packages required by pymupdf
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libxrender1 \
    libsm6 \
    libxext6 \
 && rm -rf /var/lib/apt/lists/*

# Pre-create directories
RUN mkdir -p /app/input /app/output

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY main.py .

# Run script on container start
CMD ["python", "main.py"]
