# Dockerfile

# build: docker build -t mqtt_publisher .
# run: docker run -ti mqtt_publisher

FROM python:3.12

ADD randomnumbergen.py .
ADD publisher.py .

RUN pip install paho-mqtt




CMD ["python3", "randomnumbergen.py"]