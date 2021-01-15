
# Project:   berry_case
# File:      gpio module
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

# Import modules
#############################################################################
import time
import RPi.GPIO as GPIO
import parameters
import globals
import handlers
import subprocess

# Init navigation button
#############################################################################
def init():
    # Use BCM pin numbering
    GPIO.setmode(GPIO.BCM)
    # Setup GPIOs as input with pullup resistor
    GPIO.setup(parameters.BTN_LEFT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_RIGHT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_UP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_DOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_CENTER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Create callback event for every GPIOs on falling edge. Debounce buttons.
    GPIO.add_event_detect(  parameters.BTN_LEFT_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_left_callback,
                            bouncetime=parameters.BOUNCETIME_MS)
    
    GPIO.add_event_detect(  parameters.BTN_RIGHT_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_right_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_UP_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_up_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_DOWN_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_down_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_CENTER_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_center_callback,
                            bouncetime=parameters.BOUNCETIME_MS)




