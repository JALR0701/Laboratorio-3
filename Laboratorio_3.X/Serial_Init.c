#include <stdint.h>
#include <pic16f887.h>
 #include <stdio.h>
 #include <stdlib.h>
#include "Serial_Init.h"

void initSerial(uint16_t baudrate){
    TRISC = 0x80;
    
    INTCONbits.GIE = 1;
    INTCONbits.PEIE = 1;
    
    PIE1bits.RCIE = 1;
    PIE1bits.TXIE = 1;
    
    PIR1bits.RCIF = 0;
    PIR1bits.TXIF = 0;
    
    TXSTAbits.TX9 = 0;
    TXSTAbits.TXEN = 1;
    TXSTAbits.SYNC = 0;
    TXSTAbits.BRGH = 1;
    
    RCSTAbits.SPEN = 1;
    RCSTAbits.RX9 = 0;
    RCSTAbits.CREN = 1;
    
    BAUDCTLbits.BRG16 = 1;
    
    SPBRG = ((4000000/baudrate)/4)-1;
}

void send_char (char msg){
    while (TXIF == 0);
    TXIF = 0;
    TXREG = msg;
}

void receive_char(){
    while(RCIF==0);
    RCIF=0;        
}

void ItoC (char *entero){
    int i;
	for(i=0;entero[i]!='\0';i++)//Separa los caracteres y los manda uno a uno.
	   send_char(entero[i]);
}

void sendInt (int entero){
    char buffer [4];
    sprintf (buffer, "%d", entero);
    ItoC(buffer);
}