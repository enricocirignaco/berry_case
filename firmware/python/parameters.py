
# Project:   berry_case
# File:      parameters.py
# Autor:     Enrico Cirignaco
# Created:   29.11.2020

# Import modules
#############################################################################
import subprocess


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

# gpio specific
BTN_RIGHT_GPIO = 27
BTN_LEFT_GPIO = 4
BTN_UP_GPIO = 17
BTN_DOWN_GPIO = 22
BTN_CENTER_GPIO = 23 #not working yet

# oled display specific
TOP_PADDING = 6
RIGHT_PADDING = 6
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'