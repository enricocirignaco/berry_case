
# Project:   berry_case
# File:      main program
# Autor:     Enrico Cirignaco
# Created:   22.11.2020

# Import modules
#############################################################################
import time
import oled_display
import gpio
import parameters


# Setup
#############################################################################
gpio.init()
oled_display.init()
oled_display.draw_entry(parameters.DEPTH_0_LABELS[0], parameters.MAIN_ENTRY_FONT_SIZE)

# Endless Loop
#############################################################################
try:
    while True:
        pass
except KeyboardInterrupt:
    gpio.GPIO.cleanup()
