
# Project:   berry_case
# File:      handlers
# Autor:     Enrico Cirignaco
# Created:   29.11.2020

# Import modules
#############################################################################
import time
import oled_display
import parameters
import globals
import subprocess
import fan

is_yes_state = False
is_fan_mode_auto = False

#############################################################################
# GPIO Callbacks
# Callback right button  
def btn_right_callback(arg):
    globals.display_counter = 0
    global is_yes_state
    global is_fan_mode_auto

    if globals.menu_depth == 1 and globals.main_menu_entry > 1:
        is_yes_state = False
        is_fan_mode_auto = False
        update_submenu()
    elif globals.menu_depth == 2 and globals.main_menu_entry == 4:
        if(globals.fan_speed_man < 10):
            globals.fan_speed_man+= 1
            fan.run_fan_man(globals.fan_speed_man)


# Callback left button
def btn_left_callback(arg):
    global is_yes_state
    global is_fan_mode_auto
    globals.display_counter = 0
    #if depth=0 do nothing

    if globals.menu_depth == 1:
        if globals.main_menu_entry == 0 or globals.main_menu_entry == 1:
            #if network or system submenu do nothing
            pass
        else:
            is_yes_state = True
            is_fan_mode_auto = True
            update_submenu()
    elif globals.menu_depth == 2 and globals.main_menu_entry == 4:
        if(globals.fan_speed_man > 0):
            globals.fan_speed_man-= 1
            fan.run_fan_man(globals.fan_speed_man)

# Callback down button 
def btn_down_callback(arg):
    globals.display_counter = 0

    # if in main manu scroll to next entry
    if globals.menu_depth == 0:
        if globals.main_menu_entry < parameters.MAIN_MENU_ENTRY_CNT-1:
            globals.main_menu_entry+= 1
            oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)
    elif globals.menu_depth ==1:
        #network submenu
        if globals.main_menu_entry == 0:
            if globals.network_menu_entry < parameters.NETWORK_MENU_ENTRY_CNT-1:
                globals.network_menu_entry+= 1
                oled_display.draw_entry(parameters.DEPTH_1_NETWORK_LABELS[globals.network_menu_entry], parameters.NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif globals.main_menu_entry == 1:
            if globals.system_info_menu_entry < parameters.SYSTEM_INFO_MENU_ENTRY_CNT-1:
                globals.system_info_menu_entry+= 1
                oled_display.draw_entry(parameters.DEPTH_1_SYSTEM_INFO_LABELS[globals.system_info_menu_entry], parameters.NETWORK_ENTRY_FONT_SIZE)
        
# Callback up button
def btn_up_callback(arg):
    globals.display_counter = 0

    # if in main menu scroll to previous menu
    if globals.menu_depth == 0:
        if globals.main_menu_entry > 0:
            globals.main_menu_entry-= 1
            oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)
    elif globals.menu_depth == 1:
        #network submenu
        if globals.main_menu_entry == 0:
            if globals.network_menu_entry > 0:
                globals.network_menu_entry-= 1
                oled_display.draw_entry(parameters.DEPTH_1_NETWORK_LABELS[globals.network_menu_entry], parameters.NETWORK_ENTRY_FONT_SIZE)
        # system info submenu
        elif globals.main_menu_entry == 1:
            if globals.system_info_menu_entry > 0:
                globals.system_info_menu_entry-= 1
                oled_display.draw_entry(parameters.DEPTH_1_SYSTEM_INFO_LABELS[globals.system_info_menu_entry], parameters.NETWORK_ENTRY_FONT_SIZE)

# Callback center button
def btn_center_callback(arg):
    globals.display_counter = 0
    global is_yes_state
    global is_fan_mode_auto

    # submenu depth 0
    # if in main menu go inside submenu
    if globals.menu_depth == 0:
        globals.menu_depth+= 1
        update_submenu()
    # submenu depth 1
    elif globals.menu_depth == 1:
        if globals.main_menu_entry == 0 or globals.main_menu_entry == 1:
            globals.menu_depth-= 1
            globals.network_menu_entry = 0
            globals.system_info_menu_entry = 0
            oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)
        else:
            if(is_yes_state == True and globals.main_menu_entry == 2):
                #reboot
                oled_display.draw_turn_off()
                subprocess.run("reboot", shell=True)
                exit()
            elif(is_yes_state == True and globals.main_menu_entry == 3):
                #shutdown
                oled_display.draw_turn_off()
                print("shutdown")
                subprocess.run("systemctl poweroff -i", shell=True)
                exit()
            elif(globals.main_menu_entry == 4):
                if(is_fan_mode_auto == True):
                    #set auto and escape submenu
                    globals.is_fan_auto_enabled = True
                    globals.menu_depth-= 1
                    oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)

                else:
                    #enter fan speed menu
                    globals.is_fan_auto_enabled = False
                    fan.run_fan_man(globals.fan_speed_man)
                    globals.menu_depth+= 1
            else:
                globals.menu_depth-= 1
                oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)

    # submenu depth 2
    elif(globals.menu_depth == 2):
        if(globals.main_menu_entry == 4):
            globals.menu_depth = 0
            oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)




# menu functions
#############################################################################
def update_submenu():
    global is_yes_state
    global is_fan_mode_auto
    
    if globals.main_menu_entry == 0:
        #net
        oled_display.draw_entry(parameters.DEPTH_1_NETWORK_LABELS[globals.network_menu_entry], parameters.NETWORK_ENTRY_FONT_SIZE)
    elif globals.main_menu_entry == 1:
        #system info
        oled_display.draw_entry(parameters.DEPTH_1_SYSTEM_INFO_LABELS[globals.system_info_menu_entry], parameters.SYSTEM_INFO_ENTRY_FONT_SIZE)
    # reboot submenu
    elif globals.main_menu_entry == 2 :
        oled_display.draw_selection("yes", "no", is_yes_state)

    elif globals.main_menu_entry == 3:
        oled_display.draw_selection("yes", "no", is_yes_state)

    elif globals.main_menu_entry == 4:
        oled_display.draw_selection("auto", "man", is_fan_mode_auto)
