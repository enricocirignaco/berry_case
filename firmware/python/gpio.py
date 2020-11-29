
# Project:   berry_case
# File:      gpio module
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

# Import modules
#############################################################################
import time
import RPi.GPIO as GPIO
import parameters
import globals
import handlers
import subprocess

# Init navigation button
#############################################################################
def init():
    # Use BCM pin numbering
    GPIO.setmode(GPIO.BCM)
    # Setup GPIOs as input with pullup resistor
    GPIO.setup(parameters.BTN_LEFT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_RIGHT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_UP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_DOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(parameters.BTN_CENTER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # Create callback event for every GPIOs on falling edge. Debounce buttons.
    GPIO.add_event_detect(  parameters.BTN_LEFT_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_left_callback,
                            bouncetime=parameters.BOUNCETIME_MS)
    
    GPIO.add_event_detect(  parameters.BTN_RIGHT_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_right_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_UP_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_up_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_DOWN_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_down_callback,
                            bouncetime=parameters.BOUNCETIME_MS)

    GPIO.add_event_detect(  parameters.BTN_CENTER_GPIO,
                            GPIO.FALLING,
                            callback=handlers.btn_center_callback,
                            bouncetime=parameters.BOUNCETIME_MS)











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





