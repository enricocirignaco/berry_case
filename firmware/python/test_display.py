
# Project:   berry_case
# File:      main program
# Autor:     Enrico Cirignaco
# Created:   22.11.2020

# Import modules
#############################################################################
import time
import subprocess
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from enum import Enum

# Define variables
#############################################################################
fan = 0
menu_depth = 0
main_menu_entry = 0
network_menu_entry = 0
system_info_menu_entry = 0

# Define constants
#############################################################################
BTN_RIGHT_GPIO = 27
BTN_LEFT_GPIO = 4
BTN_UP_GPIO = 22
BTN_DOWN_GPIO = 17
BTN_CENTER_GPIO = 23 #not working yet

BASH_COMMANDS = {
    "SSID":"iwgetid -r",
    "IP":"hostname -I | cut -d' ' -f1",
    "HOST":"hostname"
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
    "IP:" + subprocess.check_output(BASH_COMMANDS["IP"], shell=True).decode("utf-8"),
    "Hostname:" + subprocess.check_output(BASH_COMMANDS["HOSTNAME"], shell=True).decode("utf-8")
]
DEPTH_1_SYSTEM_INFO_LABELS = [
    "CPU Load:",
    "CPU Temp:",
    "RAM Usage:"
]
MAIN_MENU_ENTRY_CNT = len(DEPTH_0_LABELS)
NETWORK_MENU_ENTRY_CNT = len(DEPTH_1_NETWORK_LABELS)
SYSTEM_INFO_MENU_ENTRY_CNT = len(DEPTH_1_SYSTEM_INFO_LABELS)
DEBOUNCING_TIME_S = 0.5
TOP_PADDING = 6
RIGHT_PADDING = 6
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
MAIN_ENTRY_FONT_SIZE = 18
NETWORK_ENTRY_FONT_SIZE = 12
# Init Oled Display
#############################################################################
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
# Clear display.
display.fill(0)
display.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (DISPLAY_WIDTH, DISPLAY_HEIGHT))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Load default font.
# font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php

# Display functions
#############################################################################
def draw_empty():
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, DISPLAY_WIDTH-1, DISPLAY_HEIGHT-1), outline=255, fill=0)

def update_display():
    # Display image.
    display.image(image)
    display.show()

def draw_entry(entry_name, font_size):
    font = ImageFont.truetype(FONT_PATH, font_size)
    draw_empty()
    draw.text((RIGHT_PADDING, TOP_PADDING), entry_name, font=font, fill=255)
    update_display()

def draw_confirm_no():
    draw_empty()
    draw.rectangle((12,6,57,24), outline=255, fill=0)
    draw.rectangle((69,6,114,24), outline=255, fill=255)
    draw.text((17,6), "Yes", font=font, fill=255)
    draw.text((77,6), "No", font=font, fill=0)
    update_display()

def draw_confirm_yes():
    draw_empty()
    draw.rectangle((12,6,57,24), outline=255, fill=255)
    draw.rectangle((69,6,114,24), outline=255, fill=0)
    draw.text((17,6), "Yes", font=font, fill=0)
    draw.text((77,6), "No", font=font, fill=255)
    update_display()

def draw_fan_speed(speed):
    draw_empty()
    for i in range(0,speed):
        draw.rectangle((11+(11*i),6,17+(11*i),24), outline=255, fill=255)
    update_display()

def draw_fan_auto():
    draw_empty()
    draw.rectangle((12,6,57,24), outline=255, fill=255)
    draw.rectangle((69,6,114,24), outline=255, fill=0)
    draw.text((15,6), "Auto", font=font, fill=0)
    draw.text((73,6), "Man", font=font, fill=255)
    update_display()

def draw_fan_manual():
    draw_empty()
    draw.rectangle((12,6,57,24), outline=255, fill=0)
    draw.rectangle((69,6,114,24), outline=255, fill=255)
    draw.text((15,6), "Auto", font=font, fill=255)
    draw.text((73,6), "Man", font=font, fill=0)
    update_display()

# menu functions
#############################################################################
def update_submenu():
    global main_menu_entry
    is_yes_state = False
    is_fan_mode_auto = False

    if main_menu_entry == 0:
        #net
        draw_entry("SSID", MAIN_ENTRY_FONT_SIZE)
    elif main_menu_entry == 1:
        #system info
        draw_entry("CPU temp", 10)
    # reboot submenu
    elif main_menu_entry == 2 :
        if is_yes_state:
            draw_confirm_no()
        else:
            draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif main_menu_entry == 3:
        if is_yes_state:
            draw_confirm_no()
        else:
            draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif main_menu_entry == 4:
        if is_fan_mode_auto:
            draw_fan_manual()
        else:
            draw_fan_auto()
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
        draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
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
            draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
    elif menu_depth ==1:
        #network submenu
        if main_menu_entry == 0:
            if network_menu_entry < NETWORK_MENU_ENTRY_CNT-1:
                network_menu_entry+= 1
                draw_entry(DEPTH_1_NETWORK_LABELS[network_menu_entry], NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif main_menu_entry == 1:
            if system_info_menu_entry < SYSTEM_INFO_MENU_ENTRY_CNT-1:
                system_info_menu_entry+= 1
                draw_entry(DEPTH_1_SYSTEM_INFO_LABELS[system_info_menu_entry], NETWORK_ENTRY_FONT_SIZE)
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
            draw_entry(DEPTH_0_LABELS[main_menu_entry], MAIN_ENTRY_FONT_SIZE)
    elif menu_depth == 1:
        #network submenu
        if main_menu_entry == 0:
            if network_menu_entry > 0:
                network_menu_entry-= 1
                draw_entry(DEPTH_1_NETWORK_LABELS[network_menu_entry], NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif main_menu_entry == 1:
            if system_info_menu_entry > 0:
                system_info_menu_entry-= 1
                draw_entry(DEPTH_1_SYSTEM_INFO_LABELS[system_info_menu_entry], NETWORK_ENTRY_FONT_SIZE)
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




# Init navigation button
#############################################################################
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

# Setup
#############################################################################
draw_entry(DEPTH_0_LABELS[0], MAIN_ENTRY_FONT_SIZE)

# Endless Loop
#############################################################################
while True:
    pass
