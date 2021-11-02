//IR remote control RGB led
#include <IRremote.h>
#include <Adafruit_NeoPixel.h>
#define PIN 6

int RECV_PIN = 3; //This Pin should be PWM
Adafruit_NeoPixel strip = Adafruit_NeoPixel(12, PIN, NEO_GRB + NEO_KHZ800);
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{ 
  Serial.begin(9600);
  strip.begin();
  strip.show();
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  
  if (irrecv.decode(&results)) {
     	switch(results.value)
      {        
        	case 16582903:	Serial.println("1"); 	// Button 1
        			        switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(255, 0, 0), 50, 12);
				            delay(100);		//red
	          		        break;
          
        	case 16615543:  Serial.println("2"); 	// Button 2  
                        	switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(0, 0, 255), 50, 12);
				            delay(100);		//blue
	                	    break;          
          
        	case 16599223:	Serial.println("3");  	// Button 3
        			        switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(0, 255, 0), 50, 12);		
				            delay(100);		//green
				            break;
        
        	case 16591063: 	Serial.println("4"); 	// Button 4
        			        switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(255, 0, 255), 50, 12);
				            delay(100);		//magenta(r+b)
                        	break;
          
        	case 16623703:  Serial.println("5"); 	// Button 5
        			        switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(255, 255, 0), 50, 12);
				            delay(100);		//yellow(r+g)
                        	break; 
          
        	case 16607383:  Serial.println("6"); 	// Button 6
        			        switch_led(strip.Color(0, 0, 0), 0, 12);
				            switch_led(strip.Color(0, 255, 255), 50, 12);
				            delay(100);		//cyan(g+b)
                      		break;
         
 		    case 16580863:  Serial.println("OFF"); 	// Button off
				            switch_led(strip.Color(0, 0, 0), 50, 12);
				            delay(100);		//OFF
                      		break;       
        default: Serial.println(results.value);     
      }  
    irrecv.resume(); // Receive the next value
  } 
}
void switch_led(uint32_t color, int time, int led_num)
{for(uint32_t i=0; i<led_num; i++){
    strip.setPixelColor(i, color);
    strip.show();
    delay(time);
  }}