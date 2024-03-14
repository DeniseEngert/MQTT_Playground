import sys

import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")), " Topic: ", message.topic)


def get_temperatures(sender):
    mqttBroker = "mqtt.eclipseprojects.io"

    #topic_in = f"{sender}/TEMP_IN"
    #topic_out = f"{sender}/TEMP_OUT"
    topic_both = f"{sender}/#"
    #print("Receiver IN:", topic_in, " Receiver OUT:", topic_out)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(mqttBroker)

    client.loop_start()

    #tempin = client.subscribe(topic_in)
    #tempout = client.subscribe(topic_out)
    temp = client.subscribe(topic_both)
    client.on_message = on_message

    time.sleep(30)
    client.loop_stop()


if __name__ == "__main__":
    get_temperatures(sys.argv[1])
