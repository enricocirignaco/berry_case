
# Project:   berry_case
# File:      main program
# Autor:     Enrico Cirignaco
# Created:   22.11.2020

# Import modules
#############################################################################
import time
import subprocess
import oled_display
import gpio

# Define variables
#############################################################################
fan = 0
menu_depth = 0
main_menu_entry = 0
network_menu_entry = 0
system_info_menu_entry = 0

# Define constants
#############################################################################

BASH_COMMANDS = {
    "SSID":"iwgetid -r",
    "IP":"hostname -I | cut -d' ' -f1",
    "HOSTNAME":"hostname"
}
DEPTH_0_LABELS = [
    "Network",
    "System Info",
    "Reboot",
    "Power OFF",
    "Fan Settings"
]
DEPTH_1_NETWORK_LABELS =[
    "SSID:" + subprocess.check_output(BASH_COMMANDS["SSID"], shell=True).decode("utf-8"),
    subprocess.check_output(BASH_COMMANDS["IP"], shell=True).decode("utf-8"),
    subprocess.check_output(BASH_COMMANDS["HOSTNAME"], shell=True).decode("utf-8")
]
DEPTH_1_SYSTEM_INFO_LABELS = [
    "CPU Load:",
    "CPU Temp:",
    "RAM Usage:"
]
MAIN_MENU_ENTRY_CNT = len(DEPTH_0_LABELS)
NETWORK_MENU_ENTRY_CNT = len(DEPTH_1_NETWORK_LABELS)
SYSTEM_INFO_MENU_ENTRY_CNT = len(DEPTH_1_SYSTEM_INFO_LABELS)
MAIN_ENTRY_FONT_SIZE = 18
NETWORK_ENTRY_FONT_SIZE = 12

# menu functions
#############################################################################
def update_submenu():
    global main_menu_entry
    is_yes_state = False
    is_fan_mode_auto = False

    if main_menu_entry == 0:
        #net
        oled_display.draw_entry(DEPTH_1_NETWORK_LABELS[0], NETWORK_ENTRY_FONT_SIZE)
    elif main_menu_entry == 1:
        #system info
        oled_display.draw_entry("CPU temp", 10)
    # reboot submenu
    elif main_menu_entry == 2 :
        if is_yes_state:
            oled_display.draw_confirm_no()
        else:
            oled_display.draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif main_menu_entry == 3:
        if is_yes_state:
            oled_display.draw_confirm_no()
        else:
            oled_display.draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif main_menu_entry == 4:
        if is_fan_mode_auto:
            oled_display.draw_fan_manual()
        else:
            oled_display.draw_fan_auto()
        is_fan_mode_auto = not is_fan_mode_auto

#############################################################################
# GPIO Callbacks
# Callback right button  
def btn_right_callback(arg):
    global menu_depth
    global main_menu_entry
    global network_menu_entry
    global system_info_menu_entry

    # if in main menu go inside submenu
    if menu_depth == 0:
        menu_depth+= 1
        update_submenu()
    elif menu_depth == 1:
        menu_depth-= 1
        oled_display.draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
    time.sleep(gpio.DEBOUNCING_TIME_S)

# Callback left button
def btn_left_callback(arg):
    global menu_depth
    global main_menu_entry
    pass
    #if depth=0 do nothing
    time.sleep(gpio.DEBOUNCING_TIME_S)

# Callback down button 
def btn_down_callback(arg):
    global menu_depth
    global main_menu_entry
    global network_menu_entry
    global system_info_menu_entry

    # if in main manu scroll to next entry
    if menu_depth == 0:
        if main_menu_entry < MAIN_MENU_ENTRY_CNT-1:
            main_menu_entry+= 1
            oled_display.draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
    elif menu_depth ==1:
        #network submenu
        if main_menu_entry == 0:
            if network_menu_entry < NETWORK_MENU_ENTRY_CNT-1:
                network_menu_entry+= 1
                oled_display.draw_entry(DEPTH_1_NETWORK_LABELS[network_menu_entry], NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif main_menu_entry == 1:
            if system_info_menu_entry < SYSTEM_INFO_MENU_ENTRY_CNT-1:
                system_info_menu_entry+= 1
                oled_display.draw_entry(DEPTH_1_SYSTEM_INFO_LABELS[system_info_menu_entry], NETWORK_ENTRY_FONT_SIZE)
    time.sleep(gpio.DEBOUNCING_TIME_S)
        
# Callback up button
def btn_up_callback(arg):
    global menu_depth
    global main_menu_entry
    global network_menu_entry
    global system_info_menu_entry

    # if in main menu scroll to previous menu
    if menu_depth == 0:
        if main_menu_entry > 0:
            main_menu_entry-= 1
            oled_display.draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
    elif menu_depth == 1:
        #network submenu
        if main_menu_entry == 0:
            if network_menu_entry > 0:
                network_menu_entry-= 1
                oled_display.draw_entry(DEPTH_1_NETWORK_LABELS[network_menu_entry], NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif main_menu_entry == 1:
            if system_info_menu_entry > 0:
                system_info_menu_entry-= 1
                oled_display.draw_entry(DEPTH_1_SYSTEM_INFO_LABELS[system_info_menu_entry], NETWORK_ENTRY_FONT_SIZE)
    time.sleep(gpio.DEBOUNCING_TIME_S)

# Callback center button
def btn_center_callback(arg):
    global menu_depth
    global main_menu_entry
    pass
    time.sleep(gpio.DEBOUNCING_TIME_S)
    
    # if in main menu go inside submenu
    if menu_depth == 0:
        menu_depth+= 1
        #update display

# Setup
#############################################################################
gpio.init()
oled_display.init()
oled_display.draw_entry(DEPTH_0_LABELS[0], MAIN_ENTRY_FONT_SIZE)

# Endless Loop
#############################################################################
try:
    while True:
        pass
except KeyboardInterrupt:
    gpio.GPIO.cleanup()
