//Pawar.in
//Auto Intensity Control of Street Lights
const int ledPin = 2;// output control PIn
const int ldrPin = A0;// ldr pin

void setup() {
Serial.begin(9600);
pinMode(ledPin, OUTPUT);
pinMode(ldrPin, INPUT); }

void loop() {
int ldrStatus = analogRead(ldrPin);

if (ldrStatus <= 200) {
digitalWrite(ledPin, HIGH);
Serial.print("Its DARK, Turn on the LED : ");
Serial.println(ldrStatus);
} 
else {
digitalWrite(ledPin, LOW);
Serial.print("Its BRIGHT, Turn off the LED : ");
Serial.println(ldrStatus);
}
delay(500);
}