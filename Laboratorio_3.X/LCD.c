
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
#include "Serial_Init.h"
#define _XTAL_FREQ 4000000

uint8_t ready = 0, entero1 = 0, entero2 = 0, decimale1 = 0, decimale2 = 0, ttl = 0;//variables
float adc1 = 0, adc2 = 0, decimal1 = 0, decimal2 = 0;

void __interrupt() ISR (void){
    INTCONbits.GIE = 0;
    INTCONbits.PEIE = 0;
    
    if(ADCON0bits.GO_DONE == 0){//Si se realizo una conversion levantamos la bandera (se ejecua en el loop)
        ready = 1;
        PIR1bits.ADIF = 0;
    }
    
    if (PIR1bits.RCIF == 1){//Si hay datos en el puerto se leen y se guardan en una variable
        ttl = RCREG;
    }
    
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
}

void main(void) {
    TRISA = 0b00000011;// Configuracion de puertos I/O
    TRISB = 0;
    TRISC = 0;
    TRISD = 0;
    
    ANSEL = 0b00000011;
    
    PORTA = 0;//Valor inicial de los puertos
    PORTB = 0;
    PORTC = 0;
    PORTD = 0;
    
    /*initLCD ();//Inicializamos la LCD.
    lcd_clr();//Limpiar el display
    lcd_set_cursor(x,y);//Posicionar cursor
    lcd_write_string("Hola Mundo");//Escribir String*/

    initLCD(); //Inicializar LCD
    initSerial(9600);//Inicializar serial y baudrate
    lcd_clr();//Limpiar LCD
    lcd_set_cursor(1,1);//Posicionar cursor
    lcd_write_string ("POT01");//Escribir texto
    lcd_set_cursor(7,1);
    lcd_write_string ("POT02");
    lcd_set_cursor(13,1);
    lcd_write_string ("TTL");
    
    while (1){ //Loop
        initADC(0); //Inicializamos el primer canal del ADC
        if(ready){  //Guardamos el valor de la conversion
            adc1 = ADRESH;
            ready = 0;
            ADCON0bits.GO_DONE = 1;
        }
        adc1 = adc1 * 5/255;//Mapeo de 255 a 5
        entero1 = adc1;//separamos entero y decimal
        decimal1 = (adc1 - entero1)*100;
        decimale1 = decimal1;
        lcd_set_cursor(1,2);
        lcd_write_int(entero1);//escribimos el entero
        lcd_write_char('.');//escibimos caracter
        if(decimale1 >= 10){//escribimos decimal según el caso
            lcd_write_int(decimale1);
            lcd_write_string("V");
        }else{
            lcd_write_string("0");
            lcd_write_int(decimale1);
            lcd_write_string("V");
        }
        __delay_ms(20);
        
        initADC(1);//Inicializamos el segundo canal del ADC y realizamos el mismo procedimiento
        if(ready){
            adc2 = ADRESH;
            ready = 0;
            ADCON0bits.GO_DONE = 1;
        }
        adc2 = adc2 * 5/255;
        entero2 = adc2;
        decimal2 = (adc2 - entero2)*100;
        decimale2 = decimal2;
        lcd_set_cursor(7,2);
        lcd_write_int(entero2);
        lcd_write_char('.');
        if(decimale2 >= 10){
            lcd_write_int(decimale2);
            lcd_write_string("V");
        }else{
            lcd_write_string("0");
            lcd_write_int(decimale2);
            lcd_write_string("V");
        }
        __delay_ms(20);
        if(ttl >=100){// escribimos el valor recibido en el RX segun sea el caso
            lcd_set_cursor (13,2);
            lcd_write_int (ttl);    
        }else if (ttl < 100 && ttl >= 10){
            lcd_set_cursor (13,2);
            lcd_write_char('0');
            lcd_write_int (ttl);
        }else {
            lcd_set_cursor (13,2);
            lcd_write_char('0');
            lcd_write_char('0');
            lcd_write_int (ttl);
        }
        
        
        send_int(entero1);//enviamos valores por el TX y mandamos un dato para ordenar
        send_int(decimale1);
        send_int(entero2);
        send_int(decimale2);
        send_int(255);
    }
    
    return; 
}