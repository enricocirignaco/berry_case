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

# Define constants
#############################################################################
TOP_PADDING = 6
RIGHT_PADDING = 6
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

#############################################################################
# Define variables

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

#Display functions
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
