
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

#############################################################################
# GPIO Callbacks
# Callback right button  
def btn_right_callback(arg):
    globals.menu_depth
    globals.main_menu_entry
    globals.network_menu_entry
    globals.system_info_menu_entry

    # if in main menu go inside submenu
    if globals.menu_depth == 0:
        globals.menu_depth+= 1
        update_submenu()
    elif globals.menu_depth == 1:
        globals.menu_depth-= 1
        oled_display.draw_entry(parameters.DEPTH_0_LABELS[globals.main_menu_entry], parameters.MAIN_ENTRY_FONT_SIZE)

# Callback left button
def btn_left_callback(arg):
    globals.menu_depth
    globals.main_menu_entry
    pass
    #if depth=0 do nothing

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
    globals.main_menu_entry
    is_yes_state = False
    is_fan_mode_auto = False

    if globals.main_menu_entry == 0:
        #net
        oled_display.draw_entry(parameters.DEPTH_1_NETWORK_LABELS[0], parameters.NETWORK_ENTRY_FONT_SIZE)
    elif globals.main_menu_entry == 1:
        #system info
        oled_display.draw_entry("CPU temp", 10)
    # reboot submenu
    elif globals.main_menu_entry == 2 :
        if is_yes_state:
            oled_display.draw_confirm_no()
        else:
            oled_display.draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif globals.main_menu_entry == 3:
        if is_yes_state:
            oled_display.draw_confirm_no()
        else:
            oled_display.draw_confirm_yes()
        is_yes_state = not is_yes_state

    elif globals.main_menu_entry == 4:
        if is_fan_mode_auto:
            oled_display.draw_fan_manual()
        else:
            oled_display.draw_fan_auto()
        is_fan_mode_auto = not is_fan_mode_auto
