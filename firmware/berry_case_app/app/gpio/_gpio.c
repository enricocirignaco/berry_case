/**
 * @file        _gpio.c
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-12
 * @version     0.0.1
 *
 *
 * @addtogroup  Middleware
 * group description
 * @{
 */

/* Includes ------------------------------------------------------------------*/
/* HAL */
#include "gpio.h"
/* Own */
#include "_gpio.h"
//#include "config.h"
//#include "timers.h"

/* private typedef -----------------------------------------------------------*/

/* private define ------------------------------------------------------------*/

/* private macro -------------------------------------------------------------*/

/* private variables ---------------------------------------------------------*/
bool mod_Timers_tim16_flag = false;
/* public variables ----------------------------------------------------------*/

/* private function prototypes -----------------------------------------------*/

/* private functions ---------------------------------------------------------*/

/* public functions ----------------------------------------------------------*/

/**
 * Get select button value
 * Debounce Button
 */
extern bool get_Gpio_select_btn(void)
{
	if(!HAL_GPIO_ReadPin(select_btn_in_GPIO_Port, select_btn_in_Pin));
	{
		if(mod_Timers_tim16_flag)
		{
			mod_Timers_tim16_flag = false;
			return true;
		}
	}
	return false;
}

/**
 * Get power button value
 * Debounce Button
 */
extern bool get_Gpio_power_btn(void)
{
	if(!HAL_GPIO_ReadPin(power_btn_in_GPIO_Port, power_btn_in_Pin));
	{
		if(mod_Timers_tim16_flag)
		{
			mod_Timers_tim16_flag = false;
			return true;
		}
	}
	return false;
}
/**
 * read voltage from battery from ADC and calculate batery state
 */
extern bool get_Gpio_battery(void)
{
	//ADC
}
/**
 * set cooling fan speed.
 * @duty_cycle: 0-100 0--> stop fan 100--> max speed
 */
extern void set_Gpio_fan_speed(uint8_t duty_cycle)
{
	//PWM
}
/**
 * disable voltage regulator
 */
extern void set_Gpio_disable_power(void)
{
	HAL_GPIO_WritePin(power_out_GPIO_Port, power_out_Pin, false);
}

/**
 * @}
 */
