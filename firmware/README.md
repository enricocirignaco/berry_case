# setup
## Install python libraries
* Run **install_oled.sh** script in the shell
* When installation script is done **raspi-config** window will open. 
    * Navigate to **Interface Options** and enter.
    * Navigate to **I2C** and confirm with yes.
    * Exit raspi-config
* Add user to GPIO, i2c and video group:
    * sudo adduser \<username> GPIO
    * sudo adduser \<username> i2c
    * sudo adduser \<username> video
* Reboot machine by typing **sudo reboot**


### add main.py script to programms to run at startup



