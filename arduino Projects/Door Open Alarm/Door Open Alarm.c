#include <Adafruit_NeoPixel.h>
#define PIN 6
Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, PIN, NEO_GRB + NEO_KHZ800);
int tilt = 2;

void setup()
{
  pinMode(tilt, INPUT);
  pinMode(4,OUTPUT);
  strip.begin();
  strip.show();
  Serial.begin(9600);
}
 
void loop()
{
  int reading;
  reading = digitalRead(tilt);
  
  if(reading){
	switch_led(strip.Color(0, 0, 0), 50, 7);
    digitalWrite(4, LOW);
	Serial.println(reading);}
  else{
	switch_led(strip.Color(255, 0, 0), 50, 7);
    digitalWrite(4, HIGH);
    Serial.println(reading);}
}

void switch_led(uint32_t color, int time, int led_num){
  for(uint32_t i=0; i<led_num; i++){
    strip.setPixelColor(i, color);
    strip.show();
    delay(time);}}