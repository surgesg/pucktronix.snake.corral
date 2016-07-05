/***************************************************************************************

                            +-----------------+
                            |
                 +----------|---------+
       +-----------+        +         |
       +-----------+ pucktronix.matrix.switch
       +-----------+ copyleft pucktronix 2011
       +-----------+ http://www.gregsurges.com/
       +-----------+ http://bitbucket.org/pucktronix/matrix-switch/
       +-----------+                  |
       +-----------+                  |
       +-----------+                  |
       +-----------+   +++++++++      |
                 +-----|||||||||------+        OSC-controlled dual 8x8 analog switching matrix
                       |||||||||
                       |||||||||
                       +++++++++
                       
***************************************************************************************/

#define X0 PIN_F0
#define X1 PIN_F1
#define X2 PIN_F4
#define X3 PIN_F5
#define Y0 PIN_F6
#define Y1 PIN_F7
#define Y2 PIN_B6
#define DATA PIN_B5
#define STROBE PIN_B1
#define RESET PIN_B3
#define CS1 PIN_D0 // prob change later
#define CS2 PIN_B0 // prob change later

void togglePins(int chip, uint8_t x, uint8_t y, int state);

uint8_t x, y, state, first_byte;

void setup(){
  Serial.begin(9600);
  pinMode(X0, OUTPUT);  
  pinMode(X1, OUTPUT);  
  pinMode(X2, OUTPUT);  
  pinMode(X3, OUTPUT);
  digitalWrite(X3, LOW);  
  pinMode(Y0, OUTPUT);  
  pinMode(Y1, OUTPUT);  
  pinMode(Y2, OUTPUT);    
  pinMode(DATA, OUTPUT);
  pinMode(STROBE, OUTPUT);
  pinMode(RESET, OUTPUT);
  pinMode(CS1, OUTPUT);
  pinMode(CS2, OUTPUT);
  digitalWrite(RESET, HIGH);
  delay(500);
  digitalWrite(RESET, LOW);
}


void loop(){
  if(Serial.available() >= 3){
    first_byte = Serial.read();
    if(first_byte == 255){ // chip 1
      //delayMicroseconds(200);
      x = Serial.read();
      //delayMicroseconds(200);
      y = Serial.read();
      //delayMicroseconds(200);
      state = Serial.read();
      //delayMicroseconds(150);
      togglePins(CS1, x, y, state);
    } else if(first_byte == 254){ // chip 2
        //delayMicroseconds(200);
        x = Serial.read();
        //delayMicroseconds(200);
        y = Serial.read();
        //delayMicroseconds(200);
        state = Serial.read();
        //delayMicroseconds(150);
        togglePins(CS2, x, y, state);
    }   
  }
}

void togglePins(int chip, uint8_t x, uint8_t y, int state){
  if(x >= 6){ // compensate for strange x-axis addressing scheme
    x += 2;
  }
  digitalWrite(chip, HIGH);
  if(bitRead(x, 0)) digitalWrite(X0, HIGH);

  if(bitRead(x, 1)) digitalWrite(X1, HIGH);

  if(bitRead(x, 2)) digitalWrite(X2, HIGH);
  if(bitRead(x, 3)) digitalWrite(X3, HIGH);

  if(bitRead(y, 0)) digitalWrite(Y0, HIGH);  

  if(bitRead(y, 1)) digitalWrite(Y1, HIGH);  

  if(bitRead(y, 2)) digitalWrite(Y2, HIGH);  

  digitalWrite(STROBE, HIGH);

  digitalWrite(DATA, state);

  digitalWrite(STROBE, LOW);
  digitalWrite(X0, LOW);
  digitalWrite(X1, LOW);
  digitalWrite(X2, LOW);
  digitalWrite(X3, LOW);    
  digitalWrite(Y0, LOW);  
  digitalWrite(Y1, LOW);  
  digitalWrite(Y2, LOW);  
  digitalWrite(chip, LOW);
}
