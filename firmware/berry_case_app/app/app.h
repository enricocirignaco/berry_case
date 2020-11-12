
/**
 * @file        app.h
 * @brief       description
 * @author      enrico cirignaco
 * @date        2020-11-04
 * @version     0.0.1
 *
 * @addtogroup  Middleware
 * @{
 */
#ifndef APP_H
#define APP_H

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
void app_init(void);
void app_loop(void);

#ifdef __cplusplus
}
#endif

#endif /* APP_H*/

/**
 * @}
 */
