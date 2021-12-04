import urllib

import machine
#import machine import *
import dummy_threading
import time

# Create input pin
#onboard_led = machine.Pin(2)

# Create output pin
onboard_led = machine.Pin(2, machine.Pin.OUT)

def main():
    i=0
    while True:
        print("Main: {1}".format(i))
        i+=1
        time.sleep(1)

def check_reads():
    i=0
    while True:
        print("Scanning: {1}".format(i))
        i+=1
        time.sleep(3)

t=dummy_threading.Thread(check_reads,args=())
t.start()

if __name__ == '__main__':
    main()