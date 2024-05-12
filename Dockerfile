# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary development packages for building h5py
RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies common to all platforms
RUN pip install --no-cache-dir fastapi uvicorn pillow

# Install TensorFlow
RUN python -m pip install --no-cache-dir tensorflow

# Install other libraries
# Add any additional libraries you may need here

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run uvicorn when the container launches
CMD ["uvicorn", "model_pred:app", "--host", "0.0.0.0", "--port", "8000"]
