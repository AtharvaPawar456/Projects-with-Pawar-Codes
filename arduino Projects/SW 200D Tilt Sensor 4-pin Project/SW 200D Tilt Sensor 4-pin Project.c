/*
  This tilt sensor with 4 pins has a reveresed configuration compared to SW 200D tilt sensor.
  When the sensor is tilted it reads a LOW (0) value and when the sensor is not tilted it 
  reads a HIGH (1) value. 
*/

#include <Adafruit_NeoPixel.h>
#define PIN 6
Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, PIN, NEO_GRB + NEO_KHZ800);

int tilt = 7;

void setup()
{
  pinMode(tilt, INPUT);
  strip.begin();
  strip.show();
  Serial.begin(9600);
}
 
void loop()
{
  int reading;
  reading = digitalRead(tilt);
  
  if(reading){
	switch_led(strip.Color(0, 255, 0), 50, 7);
    	Serial.println(reading);}
  else{
	switch_led(strip.Color(255, 0, 0), 50, 7);
    	Serial.println(reading);}
}

void switch_led(uint32_t color, int time, int led_num){
  for(uint32_t i=0; i<led_num; i++){
    strip.setPixelColor(i, color);
    strip.show();
    delay(time);
  }
}


