Playing around with MQTT, nothing sophisticated

# without docker-compose
## Broker
#### Build
    docker build -t <name> .  

#### Start
    docker run -it -p 1883:1883 -p 9001:9001 -v <path to>/mosquitto.conf:/mosquitto/config/mosquitto.conf <container name>

## Subscriber
#### Build
    docker build -t mqtt_subscriber .

#### Run
    docker run -ti mqtt_subscriber

## Publisher
#### Build
    docker build -t mqtt_publisher .

#### Run
    docker run -ti mqtt_publisher

# with docker-compose
