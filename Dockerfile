# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies (no cache, no pip cache)
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the service port
EXPOSE 8080

# Run your app
CMD ["python", "main.py"]
