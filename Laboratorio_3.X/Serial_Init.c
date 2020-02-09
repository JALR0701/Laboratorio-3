#include <stdint.h>
#include <pic16f887.h>
 #include <stdio.h>
 #include <stdlib.h>
#include "Serial_Init.h"

void initSerial(uint16_t baudrate){
    TRISC = 0x80;
    
    /*INTCONbits.GIE = 0;
    INTCONbits.PEIE = 0;
    
    PIE1bits.RCIE = 0;
    PIE1bits.TXIE = 0;
    
    PIR1bits.RCIF = 0;
    PIR1bits.TXIF = 0;*/
    
    PIE1bits.RCIE = 0;
    
    TXSTA=0b00100110;
    
    RCSTA=0b10010000;
    
    BAUDCTLbits.BRG16 = 1;
    
    if(baudrate == 9600){
        SPBRG = 103;
    } else if (baudrate == 10417){
        SPBRG = 95;
    } else if (baudrate == 19200){
        SPBRG = 51;
    } else if (baudrate == 57600){
        SPBRG = 16;
    }
}

void send_int (int msg){
    while (TXSTAbits.TRMT == 0){
    }
    TXREG = msg;
}

//void receive_int (int ttl){
//    if (PIR1bits.RCIF == 1){
//        ttl = RCREG;
//    }
//}
