import paho.mqtt.client as mqtt

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(mqttBroker)


def send_out(topic, temp):
    client.publish(topic, temp)
    print("Just published ", str(temp) + " to topic ", topic)
    print("In wait loop")
