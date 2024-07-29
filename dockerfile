# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the main requirements.txt file into the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies from the main requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the mc-moji requirements.txt file into the container at /code/mc-moji
COPY ./app/mc-moji/requirements.txt /code/mc-moji/requirements.txt

# Install the Python dependencies from the mc-moji requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/mc-moji/requirements.txt

# Copy the rest of the application code into the container at /code
COPY ./app /code/app

# set python path to application
ENV PYTHONPATH=/code/app

# make sure there is a directory to save the images
RUN mkdir -p /code/images

# Command to run the application
CMD ["fastapi", "run", "app/main.py", "--port", "80"]


