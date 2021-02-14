# Project:   berry_case
# File:      oled display module
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

# Import modules
#############################################################################
import time
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import parameters
import globals

#############################################################################
# Define private variables
i2c	= 0
display	= 0
image = 0
draw = 0
font = ImageFont.truetype(parameters.FONT_PATH, parameters.MAIN_ENTRY_FONT_SIZE)

# Init Oled Display
#############################################################################
def init():
    global i2c	
    global display	
    global image	
    global draw
    # Create the I2C interface.
    i2c = busio.I2C(SCL, SDA)
    # Create the SSD1306 OLED class.
    # The first two parameters are the pixel width and pixel height.  Change these
    # to the right size for your display!
    display = adafruit_ssd1306.SSD1306_I2C(parameters.DISPLAY_WIDTH, parameters.DISPLAY_HEIGHT, i2c)
    # Clear display.
    display.fill(0)
    display.show()
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (parameters.DISPLAY_WIDTH, parameters.DISPLAY_HEIGHT))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Load default font.
    # font = ImageFont.load_default()
    # Alternatively load a TTF font.  Make sure the .ttf font file is in the
    # same directory as the python script!
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php

#Display functions
#############################################################################
def draw_empty():
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, parameters.DISPLAY_WIDTH-1, parameters.DISPLAY_HEIGHT-1), outline=255, fill=0)
    globals.is_display_on = True

def update_display():
    # Display image.
    display.image(image)
    display.show()

def draw_entry(entry_name, font_size):
    font = ImageFont.truetype(parameters.FONT_PATH, font_size)
    draw_empty()
    draw.text((parameters.RIGHT_PADDING, parameters.TOP_PADDING), entry_name, font=font, fill=255)
    update_display()

def draw_selection(left_selection, right_selection, is_left_selection):
    # cast boolean to 0-255
    left_selection_fill = int(is_left_selection)*255
    right_selection_fill = int(not is_left_selection)*255

    draw_empty()
    # draw boxes
    draw.rectangle((12,6,57,24), outline=255, fill=left_selection_fill)
    draw.rectangle((69,6,114,24), outline=255, fill=right_selection_fill)
    # draw text inside boxes
    draw.text((17,6), left_selection, font=font, fill=right_selection_fill)
    draw.text((77,6), right_selection, font=font, fill=left_selection_fill)
    update_display()

# speed range 0-10
def draw_fan_speed(speed):
    draw_empty()
    for i in range(0,speed):
        draw.rectangle((11+(11*i),6,17+(11*i),24), outline=255, fill=255)
    update_display()

def draw_charging_screen(charge):
    font = ImageFont.truetype(parameters.FONT_PATH, 15)
    draw_empty()

    if charge == 100:
        draw.text((32,parameters.TOP_PADDING), "Charged", font=font, fill=255)
    else:
        charge = str(charge)+"%"
        draw.text((45,8), charge, font=font, fill=255)
    update_display()

def draw_turn_off():
    draw.rectangle((0, 0, parameters.DISPLAY_WIDTH, parameters.DISPLAY_HEIGHT), outline=0, fill=0)
    globals.main_menu_entry = 0
    globals.menu_depth = 0
    globals.network_menu_entry = 0
    globals.system_info_menu_entry = 0
    globals.is_display_on = False
    update_display()