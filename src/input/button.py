import RPi.GPIO as GPIO
import time


class Button:
    def __init__(self, pin=17):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def wait_for_press(self):
        while GPIO.input(self.pin) == GPIO.HIGH:
            time.sleep(0.01)

        # debounce
        time.sleep(0.2)

    def cleanup(self):
        GPIO.cleanup()
