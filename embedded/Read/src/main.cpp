#include <Arduino.h>
#include <astraCAN.h>


//Setting up for CAN0 line
FlexCAN_T4<CAN1, RX_SIZE_256, TX_SIZE_16> Can0;

void readCan();

void setup() {


    // Initalization for using CAN with the sparkmax
    Can0.begin();
    Can0.setBaudRate(1000000);
    Can0.setMaxMB(16);
    Can0.enableFIFO();
    Can0.enableFIFOInterrupt();


}

void loop() {
  readCAN();
  delay(50);
}


void readCAN(){
  CAN_message_t msg;
  while(Can0.read(msg)){
    Serial.print("ID: ");
    Serial.print(msg.id, HEX);
    Serial.print(" ");
    Serial.print("Data: ");
    for(int i = 0; i < 8; i++){
      Serial.print(msg.buf[i], HEX);
      Serial.print(" ");
    }
    Serial.println();
  }
}