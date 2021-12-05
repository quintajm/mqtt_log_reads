import machine
import time
import micropython
from machine import *
import example_pub_button

micropython.alloc_emergency_exception_buf(100)

# Create input pin
#onboard_led = machine.Pin(2)


# Create output pin
onboard_led = machine.Pin(2, machine.Pin.OUT)

def main():
    i=0
    while True:
        onboard_led.value(0)
        time.sleep(1)
        print("Main:{}".format(i))
        i+=1
        onboard_led.value(1)
        time.sleep(1)

# Create interrupt to read
read_pin=4 #D2
pir = Pin(read_pin, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=example_pub_button)

main()

if __name__ == '__main__':
    main()