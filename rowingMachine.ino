int analogPin = 3;     
int data = 0;  
int stopFlag = 0;
int threshhold = 800;       
char userInput;
unsigned long startTime = 0;
unsigned long endTime = 0;
void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
  userInput = Serial.read();               // read user input
  if(userInput == 's'){
  data = analogRead(analogPin);    // read the input pin
    
    if(data < threshhold){  // 1000 for reed 800 for testing
      startTime = millis();
      Serial.println(data);
      
      while(stopFlag == 0){
        data = analogRead(analogPin);    // read the input pin
        
        if(Serial.available() > 0){ 
          userInput = Serial.read(); 
          
          if(userInput == 'x'){
            stopFlag = 1;
          } // if user input is 'x' to stop
          
          if(userInput == 'd'){
            if(data < threshhold){
              Serial.println(data);
             } // print if data < threshold
          } // if userInput == d
          
         } // check to see if there is user input
         
      } // while stopFlag == 0
      
      stopFlag = 0;
      endTime = millis();
      Serial.print("Total Time: ");
      Serial.println(endTime - startTime);
  
    } // first if data < 1000
  } // if user input equal to 'o'
} //if serial.available            
       
} // Void Loop
