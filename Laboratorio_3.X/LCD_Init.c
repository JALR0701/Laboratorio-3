#include <stdint.h>
#include <pic16f887.h>
#include "LCD_Init.h"



void initLCD (void){
__delay_ms(15);
//Inicialización
lcd_cmd(0x030);
__delay_ms(5);

lcd_cmd(0x030);
__delay_ms(11);

lcd_cmd(0x030);
__delay_us(160);
/////////////////
lcd_cmd(0x38);//Set interface Length
lcd_cmd(0x10);//Turn off the Display
lcd_cmd(0x01);//Clear the display
lcd_cmd(0x06);//Set cursor behavior
lcd_cmd(0x0C);//Enable display
}



void lcd_cmd(uint8_t command){
    PORTBbits.RB6 = 0;//Mandar datos. 
    PORTD = command;
    PORTBbits.RB7 = 1;
    __delay_ms(4);
    PORTBbits.RB7 = 0;
}
