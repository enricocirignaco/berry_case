  
# Project:   smartlamp
# File:      get voltage
# Autor:     Enrico Cirignaco
# Created:   27.11.2020

#############################################################################
import smbus
import time

I2C_ADDRESS = 0x68
I2C_DEVICE = 1

# config bits
READY_BIT       = 0 #1bit
CHANNEL_SEL     = 1 #2bits  channel 2
CONVERSION_MODE = 1 #1bit   continuous mode
SAMPLE_RATE_SEL = 0 #2bits  12bit resolution
PGA_GAIN_SEL    = 0 #2bits  x1 gain
config_byte = (READY_BIT<<7) | (CHANNEL_SEL<<5) | (CONVERSION_MODE<<4) | (SAMPLE_RATE_SEL<<2) | PGA_GAIN_SEL

bus = smbus.SMBus(I2C_DEVICE)
# configure device
arr = bus.read_i2c_block_data(I2C_ADDRESS, config_byte, 2)
def get_voltage_mv():
    # read raw data
    arr = bus.read_i2c_block_data(I2C_ADDRESS, config_byte, 2)
    # put the 2 received bytes together in a 16 bit variable
    adc_val = arr[1] + (arr[0]<<8)
    # calculate voltage divider
    voltage_mv = adc_val * 3
    return voltage_mv

def get_voltage_percent():
    pass
    # to be implemented
