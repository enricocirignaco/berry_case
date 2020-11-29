
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


is_yes_state = False
is_fan_mode_auto = False

#############################################################################
# GPIO Callbacks
# Callback right button  
def btn_right_callback(arg):
    globals.menu_depth
    globals.main_menu_entry
    globals.network_menu_entry
    globals.system_info_menu_entry
    global is_yes_state
    global is_fan_mode_auto

    # if in main menu go inside submenu
    if globals.menu_depth == 0:
        globals.menu_depth+= 1
        update_submenu()
    elif globals.menu_depth == 1:
        if globals.main_menu_entry == 0 or globals.main_menu_entry == 1:
            globals.menu_depth-= 1
            globals.network_menu_entry = 0
            globals.system_info_menu_entry = 0
            oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)
        else:
            is_yes_state = False
            is_fan_mode_auto = False
            update_submenu()


# Callback left button
def btn_left_callback(arg):
    global is_yes_state
    global is_fan_mode_auto
    globals.menu_depth
    globals.main_menu_entry
    #if depth=0 do nothing

    if globals.menu_depth == 1:
        if globals.main_menu_entry == 0 or globals.main_menu_entry == 1:
            #if network or system submenu do nothing
            pass
        else:
            is_yes_state = True
            is_fan_mode_auto = True
            update_submenu()

# Callback down button 
def btn_down_callback(arg):
    globals.menu_depth
    globals.main_menu_entry
    globals.network_menu_entry
    globals.system_info_menu_entry

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
    globals.menu_depth
    globals.main_menu_entry
    globals.network_menu_entry
    globals.system_info_menu_entry

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
    globals.menu_depth
    globals.main_menu_entry
    pass
    
    # if in main menu go inside submenu
    if globals.menu_depth == 0:
        globals.menu_depth+= 1
        #update display

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
