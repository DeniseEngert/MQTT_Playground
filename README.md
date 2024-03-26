Playing around with MQTT, nothing sophisticated

## Build Broker
    docker build -t <name> .  

## Start Broker
    docker run -it -p 1883:1883 -p 9001:9001 -v <path to>/mosquitto.conf:/mosquitto/config/mosquitto.conf <container name>

## Build Subscriber
    docker build -t mqtt_subscriber .

## Run Subscriber
    docker run -ti mqtt_subscriber

## Build Publisher
    docker build -t mqtt_publisher .

# Run Publisher
    docker run -ti mqtt_publisher