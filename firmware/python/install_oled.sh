
#!/bin/bash

# Update System
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools

# Set your Python install to Python 3 Default
sudo apt-get install -y python3 git python3-pip
sudo update-alternatives --install /usr/bin/python python $(which python2) 1
sudo update-alternatives --install /usr/bin/python python $(which python3) 2
sudo update-alternatives --config python

# Install Python libraries
pip3 install RPI.GPIO
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil

# Changing i2c speed from 100kHz to 1MHz
sudo cp /boot/config.txt /boot/config.txt.backup
sudo sh -c 'echo "dtparam=i2c_baudrate=1000000" >> /boot/config.txt'

# Enable i2c
echo "enable i2c and then reboot system. Afterwards you are ready to go"
sleep 3
sudo raspi-config

