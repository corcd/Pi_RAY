import RPi.GPIO as GPIO
import time

Pin = 17  # GPIO Pin 17

GPIO.setmode(GPIO.BCM)

# Setup light sensor pin status
GPIO.setup(Pin, GPIO.OUT)
GPIO.output(Pin, GPIO.LOW)
time.sleep(0.5)
GPIO.output(Pin, GPIO.HIGH)
GPIO.setup(Pin, GPIO.IN)

try:
    print("RAY On")
    while True:
        GPIO.input(Pin) == GPIO.HIGH
        time.sleep(2)

except (KeyboardInterrupt, SystemExit):
    GPIO.input(Pin) == GPIO.LOW
    GPIO.cleanup()
    print("RAY OFF")
    pass
