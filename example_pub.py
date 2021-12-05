from umqtt.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic


def main(server="10.0.0.220"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"assistant-1", b"hit")
    c.disconnect()


if __name__ == "__main__":
    main()
