#include <Adafruit_NeoPixel.h>
#define PIN 6
int force1 = 0;
int force2 = 0;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(24, PIN, NEO_GRB + NEO_KHZ800);
int num = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  strip.begin();
  strip.show();
}

void loop()
{
force1 = analogRead(A0);
force2 = analogRead(A1);
if (force1 != 0)
	{switch_led(strip.Color(255, 0, 0), 5, 24);
   	delay(100);//increace the led ON time delay accordingly
	switch_led(strip.Color(0, 0, 0), 5, 24);
    } 
if (force2 != 0)
	{switch_led(strip.Color(255, 0, 0), 5, 24);
     delay(100);//increace the led ON time delay accordingly
	switch_led(strip.Color(0, 0, 0), 5, 24);
    }
}

void switch_led(uint32_t color, int time, int led_num){
  for(uint32_t i=0; i<led_num; i++){
    strip.setPixelColor(i, color);
    strip.show();
    delay(time);}}