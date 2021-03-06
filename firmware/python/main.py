
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
import globals
import handlers


# Setup
#############################################################################
gpio.init()
oled_display.init()
parameters.update_dynamic_parameters()

oled_display.draw_entry("Berrycase v0.2", 16)
time.sleep(2)
oled_display.draw_entry(parameters.DEPTH_0_LABELS[0], parameters.MAIN_ENTRY_FONT_SIZE)

# Endless Loop
#############################################################################
try:
    while True:
        # update system and network values every second if in that submenu
        if globals.menu_depth == 1 and (globals.main_menu_entry == 0 or globals.main_menu_entry == 1):
            parameters.update_dynamic_parameters()
            handlers.update_submenu()
        
        # turn off dsplay after x seconds of inactivity
        if globals.display_counter == parameters.DISPLAY_TIMEOUT:
            oled_display.draw_turn_off()
        elif globals.display_counter < parameters.DISPLAY_TIMEOUT:
            globals.display_counter += 1
            
        time.sleep(1)
except KeyboardInterrupt:
    oled_display.draw_turn_off()
    gpio.GPIO.cleanup()
