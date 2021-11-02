//Pawar.in
//Seven segment Display basics
//we r using a Common Anode Seven Segment Display

void one(); //function existance declaration
void two();
void three();
void four();
void five();
void six();
void seven();
void eight();
void nine();

int a = 2;  //segment pin declaration
int b = 3;
int c = 4;
int d = 5;
int e = 6;
int f = 7;
int g = 8;

int t = 1000;   //delay time 

char on = HIGH;
char of = LOW;

void setup() 
{ 
  // set pin modes
  pinMode(a, OUTPUT);   //a
  pinMode(b, OUTPUT);	//b
  pinMode(c, OUTPUT);	//c
  pinMode(d, OUTPUT);	//d
  pinMode(e, OUTPUT);	//e
  pinMode(f, OUTPUT);	//f
  pinMode(g, OUTPUT);	//g
}

void loop() {
zero();
delay(t);
one();
delay(t);
two();
delay(t);
three();
delay(t);
four();
delay(t);
five();
delay(t);
six();
delay(t);
seven();
delay(t);
eight();
delay(t);
nine();
delay(t);
}

void zero() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,of);
digitalWrite(f,of);
digitalWrite(g,on);}

void one() {
digitalWrite(a,on);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,on);
digitalWrite(e,on);
digitalWrite(f,on);
digitalWrite(g,on);}

void two() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,on);
digitalWrite(d,of);
digitalWrite(e,of);
digitalWrite(f,on);
digitalWrite(g,of);}

void three() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,on);
digitalWrite(f,on);
digitalWrite(g,of);}

void four() {
digitalWrite(a,on);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,on);
digitalWrite(e,on);
digitalWrite(f,of);
digitalWrite(g,of);}

void five() {
digitalWrite(a,of);
digitalWrite(b,on);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,on);
digitalWrite(f,of);
digitalWrite(g,of);}

void six() {
digitalWrite(a,of);
digitalWrite(b,on);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,of);
digitalWrite(f,of);
digitalWrite(g,of);}

void seven() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,on);
digitalWrite(e,on);
digitalWrite(f,on);
digitalWrite(g,on);}

void eight() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,of);
digitalWrite(f,of);
digitalWrite(g,of);}

void nine() {
digitalWrite(a,of);
digitalWrite(b,of);
digitalWrite(c,of);
digitalWrite(d,of);
digitalWrite(e,on);
digitalWrite(f,of);
digitalWrite(g,of);}