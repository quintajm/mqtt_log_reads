import time
import ubinascii
import machine
from umqtt.simple import MQTTClient

# Default MQTT server to connect to
SERVER = "192.168.0.198"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"reader1"


def main(server=SERVER):

    c = MQTTClient(CLIENT_ID, server)
    c.connect()

    print("Succefull read")
    c.publish(TOPIC, b"hit")
    time.sleep_ms(200)

    c.disconnect()
