int analogPin = 3;     
int data = 0;  
int stopFlag = 0;       
char userInput;
unsigned long startTime = 0;
unsigned long endTime = 0;
void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
  
  userInput = Serial.read();               // read user input

  if(userInput == 'o'){
  data = analogRead(analogPin);    // read the input pin
    
    if(data < 800){  // 1000 for reed 800 for testing
      startTime = millis();
      Serial.println(data);

      while(data <800 && stopFlag == 0){
        Serial.println(stopFlag);
        if(Serial.available() > 0){ 
          userInput = Serial.read(); 
          if(userInput == 'x'){
            stopFlag = 1;
          }
          
        }
        
        data = analogRead(analogPin);
        Serial.println(data);
        
      } // while data < 1000
      stopFlag = 0;
      endTime = millis();
      Serial.print("Total Time: ");
      Serial.println(endTime - startTime);
  
    } // first if data < 1000
  } // if user input equal to 'e'
} //if serial.available            
       
} // Void Loop
