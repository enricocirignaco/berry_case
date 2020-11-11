/**
 * @file        app.c
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-04
 * @version     0.0.1
 *
 *
 * @addtogroup  {Driver|BSP|Middleware|Library|Module|Application}
 * group description
 * @{
 */
 
/* Includes ------------------------------------------------------------------*/
#include "app.h"
#include "main.h"
/* private typedef -----------------------------------------------------------*/

/* private define ------------------------------------------------------------*/

/* private macro -------------------------------------------------------------*/

/* private variables ---------------------------------------------------------*/
uint8_t dma_buffer[2000];
uint8_t dma_buffer_size;
UART_HandleTypeDef huart1;
DMA_HandleTypeDef hdma_usart1_rx;
/* private function prototypes -----------------------------------------------*/

/* private functions ---------------------------------------------------------*/

/* public functions ----------------------------------------------------------*/
void app_setup(void)
{
    //HAL_UART_Receive_IT(&huart1,)
    HAL_UART_Receive_DMA(&huart1, dma_buffer, dma_buffer_size);
}
void app_loop(void)
{
    
}
/**
 * @}
 */