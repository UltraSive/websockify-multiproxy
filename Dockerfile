# Use an appropriate Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script into container
COPY run-proxies.py /app/run-proxies.py

# Install dependencies
RUN pip install websockify

# Command to run the proxy
CMD ["python", "run-proxies.py"]
