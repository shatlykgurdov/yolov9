FROM python:3.9

# Set the working directory in the container
WORKDIR /yolov9

# Copy the current directory contents into the container
COPY . /yolov9

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt