
# Project:   berry_case
# File:      gpio module
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

# Import modules
#############################################################################
import time
import RPi.GPIO as GPIO

# Define constants
#############################################################################
BTN_RIGHT_GPIO = 27
BTN_LEFT_GPIO = 4
BTN_UP_GPIO = 22
BTN_DOWN_GPIO = 17
BTN_CENTER_GPIO = 23 #not working yet

# Init navigation button
#############################################################################
def init():
    GPIO.setmode(GPIO.BCM)
    # Setup GPIOs as input with pullup resistor
    GPIO.setup(BTN_RIGHT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_LEFT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_DOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_UP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_CENTER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Create callback event for every GPIOs on falling edge
    GPIO.add_event_detect(BTN_RIGHT_GPIO, GPIO.FALLING)
    GPIO.add_event_detect(BTN_LEFT_GPIO, GPIO.FALLING)
    GPIO.add_event_detect(BTN_DOWN_GPIO, GPIO.FALLING)
    GPIO.add_event_detect(BTN_UP_GPIO, GPIO.FALLING)
    GPIO.add_event_detect(BTN_CENTER_GPIO, GPIO.FALLING)
    # Define callback functions to be called
    GPIO.add_event_callback(BTN_DOWN_GPIO, btn_up_callback)
    GPIO.add_event_callback(BTN_UP_GPIO, btn_down_callback)
    GPIO.add_event_callback(BTN_RIGHT_GPIO, btn_right_callback)
    GPIO.add_event_callback(BTN_LEFT_GPIO, btn_left_callback)
    GPIO.add_event_callback(BTN_CENTER_GPIO, btn_center_callback)




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
    time.sleep(DEBOUNCING_TIME_S)

# Callback left button
def btn_left_callback(arg):
    global menu_depth
    global main_menu_entry
    pass
    #if depth=0 do nothing
    time.sleep(DEBOUNCING_TIME_S)

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
    time.sleep(DEBOUNCING_TIME_S)
        
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
    time.sleep(DEBOUNCING_TIME_S)

# Callback center button
def btn_center_callback(arg):
    global menu_depth
    global main_menu_entry
    pass
    time.sleep(DEBOUNCING_TIME_S)
    
    # if in main menu go inside submenu
    if menu_depth == 0:
        menu_depth+= 1
        #update display










#############################################################################
# get data functions
# Shell scripts for system monitoring from here:
# https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load

def get_system_ip():
    cmd = "hostname -I | cut -d' ' -f1"
    ip = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return ip
def get_system_cpu():
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    cpu = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return cpu
def get_system_memory():
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    mem = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return mem
def get_system_disk():
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return disk
def get_system_hostname():
    cmd = "hostname"
    hostname = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return hostname
def get_system_ssid():
    cmd = "iwgetid -r"
    ssid = subprocess.check_output(cmd, shell=True).decode("utf-8")
    return ssid





