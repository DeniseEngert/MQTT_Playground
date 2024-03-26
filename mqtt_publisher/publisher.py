import paho.mqtt.client as mqtt

#mqttBroker = "mqtt.eclipseprojects.io"
mqttBroker = "127.0.0.1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(mqttBroker)


def send_out(topic, temp):
    ret = client.publish(topic, temp)
    print("Return: ", ret[0], "   ", ret[1])
    print("Just published ", str(temp) + " to topic ", topic)
    print("In wait loop")
