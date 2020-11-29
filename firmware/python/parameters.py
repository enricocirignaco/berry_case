
# Project:   berry_case
# File:      parameters.py
# Autor:     Enrico Cirignaco
# Created:   29.11.2020

# Import modules
#############################################################################
import subprocess


BASH_COMMANDS = {
    "SSID": "iwgetid -r",
    "IP": "hostname -I | cut -d' ' -f1",
    "HOSTNAME": "hostname",
    "CPU": "top -bn1 | grep load | awk '{printf \"%.2f%%\", $(NF-2)}'",
    "CPU_TEMP": "cat /sys/class/thermal/thermal_zone0/temp | awk '{printf \"%.2f\", $1/1000}'",
    "GPU_TEMP": "/opt/vc/bin/vcgencmd measure_temp | cut -d '=' -d '=' -f2 | cut -d \\' -f1",
    "MEMORY": "free -m | awk 'NR==2{printf \"%.2f%%\", $3*100/$2 }'",
    "DISK": 'df -h | awk \'$NF=="/"{printf "%d/%dGB  %s", $3,$2,$5}\'',
    "REBOOT": "sudo reboot",
    "SHUTDOWN": "sudo shutdown now"

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
    "Host:" + subprocess.check_output(BASH_COMMANDS["HOSTNAME"], shell=True).decode("utf-8")
]
DEPTH_1_SYSTEM_INFO_LABELS = [
    "CPU Load: " + subprocess.check_output(BASH_COMMANDS["CPU"], shell=True).decode("utf-8"),
    "CPU Temp: " + subprocess.check_output(BASH_COMMANDS["CPU_TEMP"], shell=True).decode("utf-8"),
    "GPU Temp: " + subprocess.check_output(BASH_COMMANDS["GPU_TEMP"], shell=True).decode("utf-8"),
    "Memory: " + subprocess.check_output(BASH_COMMANDS["MEMORY"], shell=True).decode("utf-8"),
    "Disk: " + subprocess.check_output(BASH_COMMANDS["DISK"], shell=True).decode("utf-8")
]
MAIN_MENU_ENTRY_CNT = len(DEPTH_0_LABELS)
NETWORK_MENU_ENTRY_CNT = len(DEPTH_1_NETWORK_LABELS)
SYSTEM_INFO_MENU_ENTRY_CNT = len(DEPTH_1_SYSTEM_INFO_LABELS)
MAIN_ENTRY_FONT_SIZE = 18
NETWORK_ENTRY_FONT_SIZE = 12
SYSTEM_INFO_ENTRY_FONT_SIZE = 12


# gpio specific
BTN_RIGHT_GPIO = 27
BTN_LEFT_GPIO = 4
BTN_UP_GPIO = 17
BTN_DOWN_GPIO = 22
BTN_CENTER_GPIO = 23 #not working yet
BOUNCETIME_MS = 200
# oled display specific
TOP_PADDING = 6
RIGHT_PADDING = 6
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 32
FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

def update_dynamic_parameters():
    global DEPTH_1_NETWORK_LABELS
    global DEPTH_1_SYSTEM_INFO_LABELS

    DEPTH_1_NETWORK_LABELS =[
        "SSID:" + subprocess.check_output(BASH_COMMANDS["SSID"], shell=True).decode("utf-8"),
        subprocess.check_output(BASH_COMMANDS["IP"], shell=True).decode("utf-8"),
        "Host:" + subprocess.check_output(BASH_COMMANDS["HOSTNAME"], shell=True).decode("utf-8")
    ]
    DEPTH_1_SYSTEM_INFO_LABELS = [
        "CPU Load: " + subprocess.check_output(BASH_COMMANDS["CPU"], shell=True).decode("utf-8"),
        "CPU Temp: " + subprocess.check_output(BASH_COMMANDS["CPU_TEMP"], shell=True).decode("utf-8"),
        "GPU Temp: " + subprocess.check_output(BASH_COMMANDS["GPU_TEMP"], shell=True).decode("utf-8"),
        "Memory: " + subprocess.check_output(BASH_COMMANDS["MEMORY"], shell=True).decode("utf-8"),
        "Disk: " + subprocess.check_output(BASH_COMMANDS["DISK"], shell=True).decode("utf-8")
    ]