
# Project:   berry_case
# File:      main program
# Autor:     Enrico Cirignaco
# Created:   22.11.2020

# import modules
#############################################################################
import time
import subprocess
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from enum import Enum

#############################################################################
# Define variables
top_padding = 6
right_padding = 6
display_ptr = 'network'
fan = 0
menu_depth = 0
menu_entry = 0
MENU_ENTRY_CNT = 5
DEPTH_0_LABELS = [
    "Network",
    "System Info",
    "Reboot",
    "Power OFF",
    "Fan Settings"
]
class current_position(Enum):
    MAIN_NETWORK = 1
    MAIN_SYSTEM_INFO = 2
    MAIN_REBOOT = 3
    MAIN_POWER_OFF = 4
    MAIN_FAN_SETTINGS = 5
    MAIN_CHARGING = 6
    FAN_SETTINGS_AUTO_MAN = 7

#############################################################################
# Init navigation button
btn_right_gpio = 27
btn_left_gpio = 4
btn_up_gpio = 17
btn_down_gpio = 22
btn_center_gpio = 2 #to be changed

GPIO.setmode(GPIO.BCM)
# Setup GPIOs as INout with pullup resistor
GPIO.setup(btn_right_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_left_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_up_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_down_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_center_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Create callback event for every GPIOs
GPIO.add_event_detect(btn_right_gpio, GPIO.FALLING)
GPIO.add_event_detect(btn_left_gpio, GPIO.FALLING)
GPIO.add_event_detect(btn_up_gpio, GPIO.FALLING)
GPIO.add_event_detect(btn_down_gpio, GPIO.FALLING)
GPIO.add_event_detect(btn_center_gpio, GPIO.FALLING)

#############################################################################
# Init Oled Display
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Clear display.
display.fill(0)
display.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = display.width
height = display.height
image = Image.new("1", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Load default font.
# font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)

#############################################################################
# functions
def draw_empty():
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width-1, height-1), outline=255, fill=0)

def update_display():
    # Display image.
    display.image(image)
    display.show()

def draw_entry(title):
    draw_empty()
    draw.text((right_padding, top_padding), title, font=font, fill=255)
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




def logic():
    global menu_depth
    global menu_entry
    
def btn_right_callback(arg):
    pass
    #if depth=0 do nothing

def btn_left_callback():
    pass
    #if depth=0 do nothing
        
def btn_down_callback():
    if menu_depth == 0:
        if menu_entry < MENU_ENTRY_CNT-1:
            menu_entry+= 1
            draw_entry(DEPTH_0_LABELS[menu_entry])

def btn_up_callback():
    if menu_depth == 0:
        if menu_entry > 0:
            menu_entry+= 1
            draw_entry(DEPTH_0_LABELS[menu_entry])

def btn_center_callback():
    if menu_depth == 0:
        menu_depth+= 1
        #update display
         
GPIO.add_event_callback(btn_up_gpio, btn_up_callback)
GPIO.add_event_callback(btn_down_gpio, btn_down_callback)
GPIO.add_event_callback(btn_right_gpio, btn_right_callback)
GPIO.add_event_callback(btn_left_gpio, btn_left_callback)
GPIO.add_event_callback(btn_center_gpio, btn_center_callback)

#############################################################################
# Endless loop
while True:
    draw_confirm_no()
    time.sleep(2)
    draw_confirm_yes()
    time.sleep(2)
