# Use an official Python runtime as the base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libcurl4-openssl-dev \
    libssl-dev \
    libffi-dev \
    build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the current directory content into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

#ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-key.json"

# Command to run the Python script
CMD ["python", "download_upload_load.py"]


