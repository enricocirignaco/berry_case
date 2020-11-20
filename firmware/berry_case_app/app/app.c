/**
 * @file        app.c
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
#include "app.h"
#include "fsm.h"
//#include "main.h"
/* private typedef -----------------------------------------------------------*/

/* private define ------------------------------------------------------------*/

/* private macro -------------------------------------------------------------*/

/* private variables ---------------------------------------------------------*/
uint8_t dma_buffer[2000];
uint8_t dma_buffer_size;
//UART_HandleTypeDef huart1;
//DMA_HandleTypeDef hdma_usart1_rx;
/* private function prototypes -----------------------------------------------*/

/* private functions ---------------------------------------------------------*/

/* public variables ----------------------------------------------------------*/

/* public functions ----------------------------------------------------------*/
/*
 * Application setup
 * To run just one time in main
 */
void app_init(void)
{
	//init modules here

	// Set initial mode.

	// delay while raspberry is starting

	// set beginning state
	mod_fsm_state = DISPLAY_BATTERY;
	
}

/*
 * Application Routine
 * To run in the endless loop
 */
void app_loop(void)
{
	//run FSM
	sh_mod_fsm_function_ptr[mod_fsm_state]();
}
 /**
 * @}
 */
