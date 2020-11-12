
/**
 * @file        _gpio.h
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-12
 * @version     0.0.1
 *
 * @addtogroup  Middleware
 * @{
 */
#ifndef FSM_H_
#define FSM_H_

#ifdef __cplusplus
 extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
/* standard libraries */
#include <stdint.h>
#include <stdbool.h>

/* exported typedef ----------------------------------------------------------*/

/* exported define -----------------------------------------------------------*/

/* exported macro ------------------------------------------------------------*/

/* exported variables --------------------------------------------------------*/

/* exported function prototypes ----------------------------------------------*/
extern bool get_Gpio_select_btn(void);
extern bool get_Gpio_power_btn(void);
extern bool get_Gpio_battery(void);
extern void set_Gpio_fan_speed(uint8_t duty_cycle);
extern void set_Gpio_disable_power(void);

#ifdef __cplusplus
}
#endif

#endif /* GPIOO_H_ */

