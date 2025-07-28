# Use Python 3.10 slim base image and ensure amd64 architecture
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies (offline-safe, no cache)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application code
COPY main.py .

# Create input/output folders inside container
RUN mkdir input output

# Set default command to run your script
CMD ["python", "main.py"]
