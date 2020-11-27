
# Project:   berry_case
# File:      gpio module
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

# Import modules
#############################################################################
import time
import RPi.GPIO as GPIO
import test_display
import subprocess

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
    GPIO.add_event_callback(BTN_DOWN_GPIO, test_display.btn_up_callback)
    GPIO.add_event_callback(BTN_UP_GPIO, test_display.btn_down_callback)
    GPIO.add_event_callback(BTN_RIGHT_GPIO, test_display.btn_right_callback)
    GPIO.add_event_callback(BTN_LEFT_GPIO, test_display.btn_left_callback)
    GPIO.add_event_callback(BTN_CENTER_GPIO, test_display.btn_center_callback)

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





