
/**
 * @file        fsm.h
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-04
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

/* exported typedef -----------------------------------------------------------*/
// define type for a pointer of a function
typedef void(*mod_fsm_function_ptr_t)(void);

// define type for fsm state counter
typedef enum{
	DISPLAY_BATTERY		= 0x01,
	DISPLAY_IP_ADDR		= 0x02,
	DISPLAY_CPU_TEMP	= 0x03,
	DISPLAY_FAN_SPEED	= 0x04,
	IDLE				= 0x05,
	SHUTDOWN			= 0x06
}mod_fsm_state_t;

/* exported define -----------------------------------------------------------*/

/* exported macro ------------------------------------------------------------*/

/* exported variables --------------------------------------------------------*/
extern mod_fsm_state_t mod_fsm_state;
extern mod_fsm_function_ptr_t sh_mod_fsm_function_ptr[0x06];

/* exported structures -------------------------------------------------------*/

/* exported function prototypes ----------------------------------------------*/

#ifdef __cplusplus
}
#endif

#endif /* FSM_H_*/

/**
 * @}
 */
