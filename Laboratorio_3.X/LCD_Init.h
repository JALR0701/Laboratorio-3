/* 
 * File:   LCD_Init.h
 * Author: jorge
 *
 * Created on 5 de febrero de 2020, 01:39 PM
 */

#ifndef LCD_INIT_H
#define	LCD_INIT_H

#include <xc.h>
#include <stdint.h>
#define _XTAL_FREQ 4000000

void initLCD (void);
void lcd_cmd ();
void lcd_clr (void);
void lcd_write_char(unsigned char var);
void lcd_rst_cursor(void);

#endif	/* LCD_INIT_H */

