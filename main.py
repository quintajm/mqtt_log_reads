import urllib
import machine
import uasyncio
import time
import micropython
micropython.alloc_emergency_exception_buf(100)

# Create input pin
#onboard_led = machine.Pin(2)

# Create output pin
onboard_led = machine.Pin(2, machine.Pin.OUT)

async def main():
    i=0
    task = uasyncio.create_task(check_reads(1))
    while True:
        onboard_led.value(0)
        time.sleep(1)
        print("Main:{}".format(i))
        i+=1
        onboard_led.value(1)
        time.sleep(1)
        await task

# Create async callback
async def check_reads(pin,t):
    i=1
    while True:
        print("Scanning: {}".format(i))
        i+=1
        time.sleep(t)

uasyncio.run(main())

if __name__ == '__main__':
    main()