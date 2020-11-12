/**
 * @file        fsm.c
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-04
 * @version     0.0.1
 *
 *
 * @addtogroup  Middleware
 * group description
 * @{
 */

/* Includes ------------------------------------------------------------------*/
#include "fsm.h"
#include "Gpio.h"
/* private typedef -----------------------------------------------------------*/

/* private define ------------------------------------------------------------*/

/* private macro -------------------------------------------------------------*/

/* private variables ---------------------------------------------------------*/

/* private function prototypes -----------------------------------------------*/
void mod_fsm_state_display_battery(void);
void mod_fsm_state_display_ip_addr(void);
void mod_fsm_state_display_cpu_temp(void);
void mod_fsm_state_display_fan_speed(void);
void mod_fsm_state_idle(void);
void mod_fsm_state_shutdown(void);

/* public functions ----------------------------------------------------------*/

/* public variables ----------------------------------------------------------*/
//Pointer FSM function
mod_fsm_function_ptr_t sh_mod_fsm_function_ptr[0x06] =
{
	mod_fsm_state_display_battery,
	mod_fsm_state_display_ip_addr,
	mod_fsm_state_display_cpu_temp,
	mod_fsm_state_display_fan_speed,
	mod_fsm_state_idle,
	mod_fsm_state_shutdown
};
// current state FSM
mod_fsm_state_t mod_fsm_state;

/* private functions ---------------------------------------------------------*/
/* start FSM -----------------------------------------------------------------*/
/*
 * state display battery
 */
void mod_fsm_display_battery(void)
{
		mod_fsm_state = DISPLAY_IP_ADDR;
		uint8_t x= get_Gpio_select_btn();
}

void mod_fsm_state_display_battery(void)
{

}
void mod_fsm_state_display_ip_addr(void)
{

}
void mod_fsm_state_display_cpu_temp(void)
{

}
void mod_fsm_state_display_fan_speed(void)
{

}
void mod_fsm_state_idle(void)
{

}
void mod_fsm_state_shutdown(void)
{
	
}
/* public functions ----------------------------------------------------------*/
    

/**
 * @}
 */
