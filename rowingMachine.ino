int analogPin = 3;     
int data = 0;  
int stopFlag = 0;
int threshhold = 800;
int upRow = 0;
int downRow = 0;
int rowFlag = 0;       
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
            data = analogRead(analogPin);
            if(data < threshhold){
              upRow = 1;
              Serial.print("Got Up Row: ");
              Serial.println(data);
              while(data < threshhold){
                data = analogRead(analogPin);
                Serial.print("Waiting in up row: ");
                Serial.println(data);
                delay(1000);
              }
            }
              if(upRow == 1){
                upRow = 0;
                 Serial.print("Got Mid Row");
              // if data is greater or equal to threshold
                while(data >= threshhold){
                  data = analogRead(analogPin);
                  Serial.print("In Mid row!: ");
                  Serial.println(data);
                  delay(1000);
                  
                } // NOP wait loop
                Serial.print("Full Row Done!");
          } // while rowFlag is False
          Serial.println("rowFlag is False, out of the loop");
         } // check to see if there is user input 'd'
         Serial.println("in userInput Loop");
      } // if SerialAvailable 
    }// while stopFlag == 0
      Serial.println("Got Stop Flag");
      stopFlag = 0;
      endTime = millis();
      Serial.print("Total Time: ");
      Serial.println(endTime - startTime);
  
  } // if user input equal to 's'
} //if serial.available            
       
} // Void Loop
