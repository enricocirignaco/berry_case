# Project:   berry_case
# File:      fan.py
# Autor:     Enrico Cirignaco
# Created:   05.12.2020

# Import modules
#############################################################################
import oled_display
import gpio

def run_fan_auto():
    #set auto
    pass

#speed between 0 and 10
def run_fan_man(speed):
    oled_display.draw_fan_speed(speed)
    
