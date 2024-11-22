void setup() {
  Serial.begin(9600);
}

void loop() {
  int soundLevel = analogRead(A0);
  Serial.println(soundLevel);
  delay(100);
}

