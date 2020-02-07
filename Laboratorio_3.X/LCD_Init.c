#include <stdint.h>
#include <pic16f887.h>
#include "LCD_Init.h"



void initLCD (void){
__delay_ms(15);
PORTD = 0x030;
__delay_ms(5);
PORTD = 0x030;
__delay_us(160);
PORTD = 0x030;
__delay_us(160);

PORTBbits.RB6 = 0; //Entrar a modo comando.
PORTBbits.RB7 = 0;
__delay_us(160);

PORTD = 60; //Asigna el tamaño de la interfaz.
lcd_cmd();

PORTD = 1; // Limpiar el display.
PORTBbits.RB6 = 0;//Mandar datos. 
PORTBbits.RB7 = 0;
__delay_ms(1.64);
PORTBbits.RB7 = 0;

PORTD = 7;//Asigna el comportamiento del cursor.
lcd_cmd();

PORTD = 15; //Habilita el cursor y el display.
lcd_cmd();
}



void lcd_cmd(){
    PORTBbits.RB6 = 0;//Mandar datos. 
    PORTBbits.RB7 = 0;
    __delay_us(40);
    PORTBbits.RB7 = 0;
}

/*void lcd_clr (void){
    PORTD = 1;// LImpiar display.
    lcd_cmd();
}

void lcd_write_char(unsigned char var){
    PORTBbits.RB6 = 1;// Escribir datos.
    PORTD = var;
    PORTBbits.RB7 = 1;
    __delay_ms(4);
    PORTBbits.RB7 = 0;
}

void lcd_rst_cursor(void) {
    PORTD = 2;
    lcd_cmd();    
}*/