# Project:      berry_case
# File:         autostart.sh
# Autor:        Enrico Cirignaco
# Created:      11.12.2020
# Description:  This script need to be added to the crontab of the pi user.
#               crontab -e --> @reboot /home/dev/documents/berry_case/firmware/python/autostart.sh
#               This script just run the main Python script wit sudo rights in background.


#!/bin/bash
cd /home/dev/documents/berry_case/firmware/python/
sudo -E python3 ./main.py &