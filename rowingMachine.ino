int analogPin = 3;     
int data = 0;  
int stopFlag = 0;
int threshhold = 800;
int upRow = 0;
int downRow = 0;
int passCount = 0;       
char userInput;
unsigned long startTime = 0;
unsigned long endTime = 0;
#define NOP __asm__ __volatile__ ("nop\n\t")

void setup(){

  Serial.begin(9600);                        //  setup serial

}

void loop(){

if(Serial.available()> 0){ 
  userInput = Serial.read();               // read user input
  
  if(userInput == 's'){
    startTime = millis();
    
    while(stopFlag == 0){
       data = analogRead(analogPin);    // read the input pin
        
       if(Serial.available() > 0){ 
         userInput = Serial.read(); 
          
         if(userInput == 'x'){
           stopFlag = 1;
          } // if user input is 'x' to stop
          
         if(userInput == 'd'){
           
           while(passCount < 2){
            data = analogRead(analogPin);
            if(data < threshhold){
              upRow = 1;
              Serial.println("Got Up Row");
              while(data < threshhold){
                NOP;
              }
              passCount = passCount + 1; 
              } // print if data < threshold
           } // Check passCount
           passCount = 0;
          } // if userInput == d
          
         } // check to see if there is user input
         
      } // while stopFlag == 0
      
      stopFlag = 0;
      endTime = millis();
      Serial.print("Total Time: ");
      Serial.println(endTime - startTime);
  
  } // if user input equal to 'o'
} //if serial.available            
       
} // Void Loop
