
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "printf.h"

//
// Hardware configuration
//


RF24 radio(8,10);

void setup(void){

    radio.begin();
    radio.setPALevel(RF_24_PA_MAX);
    radio.setChannel(0x75);
    radio.openWritingPipe(0xF0F0F0F0E1LL);
    radio.enableDynamicPayloads();
    radio.powerUp();

}

void loop(void){

    const char text[] = "girish ramnani";
    radio.write(text,sizeof(text));


}
