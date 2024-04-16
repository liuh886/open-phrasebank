# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code from your host to your image filesystem.
COPY . .

# No need for EXPOSE if you are not running a service.

# No CMD is needed either, but you could use CMD ["python"] to start a Python shell
CMD ["python"]