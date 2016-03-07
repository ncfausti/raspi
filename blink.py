import RPi.GPIO as GPIO
import time

LED = 17

GPIO.setmode(GPIO.BCM)     # Set to board numbering
GPIO.setup(LED, GPIO.OUT)  # Setup LED channel for output
GPIO.output(LED, GPIO.LOW)  # Initialize output state to low

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print 'Exiting'
    GPIO.cleanup()
