
# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time
import subprocess
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
top_padding = 6
right_padding = 6
gpio = 16
display_ptr = 'network'

# Load default font.
#font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(gpio, GPIO.FALLING)


def draw_empty():
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width-1, height-1), outline=255, fill=0)

def update_display():
    # Display image.
    disp.image(image)
    disp.show()

def draw_network():
    draw_empty()
    draw.text((right_padding, top_padding), "Network", font=font, fill=255)
    global display_ptr
    display_ptr = 'network'

def draw_system_info():
    draw_empty()
    draw.text((right_padding, top_padding), "System Info", font=font, fill=255)
    global display_ptr
    display_ptr = 'system_info'

def draw_reboot():
    draw_empty()
    draw.text((right_padding, top_padding), "Reboot", font=font, fill=255)
    global display_ptr
    display_ptr = 'reboot'

def draw_power_off():
    draw_empty()
    draw.text((right_padding, top_padding), "Power OFF", font=font, fill=255)
    global display_ptr
    display_ptr = 'power_off'

def draw_fan_settings():
    draw_empty()
    draw.text((right_padding, top_padding), "Fan Settings", font=font, fill=255)
    global display_ptr
    display_ptr = 'fan_settings'
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
    for speed in range(0,10):
        draw.rectangle((10+(10*speed),6,20+(10*speed),24), outline=255, fill=255)
    update_display()


def btn_callback(arg):
    global display_ptr
    print(display_ptr)

    if display_ptr == 'network':
        draw_system_info()
    elif display_ptr == 'system_info':
        draw_reboot()
    elif display_ptr == 'reboot':
        draw_power_off()
    elif display_ptr == 'power_off':
        draw_fan_settings()
    elif display_ptr == 'fan_settings':
        draw_network()
    update_display()

    #debouncing button
    time.sleep(0.5)
    
GPIO.add_event_callback(gpio, btn_callback)
#draw_network()
#update_display()

while True:
    draw_confirm_yes()
    time.sleep(2)
    #draw_confirm_no()
    draw_fan_speed()
    time.sleep(2)