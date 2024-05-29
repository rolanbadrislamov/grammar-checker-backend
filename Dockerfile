# Use a lightweight base image
FROM python:3.10.6-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV FASTAPI_ENV production

# Set working directory
WORKDIR /api_code

# Copy requirements file and install dependencies
COPY ./requirements.txt /api_code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /api_code

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
