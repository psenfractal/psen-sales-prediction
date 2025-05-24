# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
COPY create_artifact_repo.py .
RUN pip install --no-cache-dir -r requirements.txt
RUN python create_artifact_repo.py

# Copy the current directory contents into the container
COPY . /app

# Expose the port the app will run on
EXPOSE 8080

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

