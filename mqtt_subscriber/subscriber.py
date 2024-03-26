import sys

import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")), " Topic: ", message.topic)


def get_temperatures(sender):
    #mqttBroker = "mqtt.eclipseprojects.io"
    mqttBroker = "127.0.0.1"

    #topic_in = f"{sender}/TEMP_IN"
    #topic_out = f"{sender}/TEMP_OUT"
    topic_both = f"{sender}/#"

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(mqttBroker)

    client.loop_start()

    temp = client.subscribe(topic_both)
    client.on_message = on_message

    time.sleep(30)
    client.loop_stop()


if __name__ == "__main__":
    get_temperatures(sys.argv[1])
