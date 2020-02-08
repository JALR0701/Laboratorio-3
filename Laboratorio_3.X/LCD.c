
// PIC16F887 Configuration Bit Settings

// 'C' source line config statements

// CONFIG1
#pragma config FOSC = INTRC_NOCLKOUT// Oscillator Selection bits (INTOSCIO oscillator: I/O function on RA6/OSC2/CLKOUT pin, I/O function on RA7/OSC1/CLKIN)
#pragma config WDTE = OFF       // Watchdog Timer Enable bit (WDT disabled and can be enabled by SWDTEN bit of the WDTCON register)
#pragma config PWRTE = OFF      // Power-up Timer Enable bit (PWRT disabled)
#pragma config MCLRE = OFF      // RE3/MCLR pin function select bit (RE3/MCLR pin function is digital input, MCLR internally tied to VDD)
#pragma config CP = OFF         // Code Protection bit (Program memory code protection is disabled)
#pragma config CPD = OFF        // Data Code Protection bit (Data memory code protection is disabled)
#pragma config BOREN = OFF      // Brown Out Reset Selection bits (BOR disabled)
#pragma config IESO = OFF       // Internal External Switchover bit (Internal/External Switchover mode is disabled)
#pragma config FCMEN = OFF      // Fail-Safe Clock Monitor Enabled bit (Fail-Safe Clock Monitor is disabled)
#pragma config LVP = OFF        // Low Voltage Programming Enable bit (RB3 pin has digital I/O, HV on MCLR must be used for programming)

// CONFIG2
#pragma config BOR4V = BOR40V   // Brown-out Reset Selection bit (Brown-out Reset set to 4.0V)
#pragma config WRT = OFF        // Flash Program Memory Self Write Enable bits (Write protection off)

// #pragma config statements should precede project file includes.
// Use project enums instead of #define for ON and OFF.

#include <xc.h>
#include <stdint.h>
#include "LCD_Init.h"
#include "ADC_Init.h"
#define _XTAL_FREQ 4000000

uint8_t ready = 0, adc = 0, adc2 = 0;
float decimal = 0, voltaje = 0;

void __interrupt() ISR (void){
    INTCONbits.GIE = 0;
    INTCONbits.PEIE = 0;
    
    if(ADCON0bits.GO_DONE == 0){
        ready = 1;
        PIR1bits.ADIF = 0;
    }
    
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
}

void main(void) {
    TRISA = 0b00000011;
    TRISB = 0;
    TRISC = 0;
    TRISD = 0;
    
    ANSEL = 0b00000011;
    
    
    PORTA = 0;
    PORTB = 0;
    PORTC = 0;
    PORTD = 0;
    
    /*initLCD ();//Inicializamos la LCD.
    lcd_clr();//Limpiar el display
    lcd_set_cursor(x,y);//Posicionar cursor
    lcd_write_string("Hola Mundo");//Escribir String*/

    initLCD();
    initADC(0);
    lcd_write_string("Hola Mundo");
    __delay_ms(1000);
    lcd_clr();
    lcd_write_int(255);
    __delay_ms(1000);
    lcd_clr();
    
    while (1){ //Loop
        initADC(0);
        if(ready){
            adc = ADRESH * 5/255;
            ready = 0;
            ADCON0bits.GO_DONE = 1;
        }
        PORTC = adc;
        lcd_set_cursor (1,1);
        lcd_write_float(adc);
    }
    
    return; 
}