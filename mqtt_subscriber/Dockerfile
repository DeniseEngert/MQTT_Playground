# Dockerfile

# build: docker build -t mqtt_subscriber .
# run: docker run -ti mqtt_subscriber

FROM python:3.12

ADD subscriber1.py .

RUN pip install paho-mqtt




CMD ["python3", "subscriber.py"]