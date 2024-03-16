char dato;

void setup() {
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0){
    dato = Serial.read();
    if(dato == '1'){
      digitalWrite(7, HIGH);
    }
    if(dato == '0'){
      digitalWrite(7, LOW);
    }
  }
}