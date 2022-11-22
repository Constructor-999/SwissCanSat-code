

void setup() {
  Serial.begin(2000000);
  Serial.setTimeout(0.0001);
}

void loop() {
  if (Serial.available() > 0) {
      String str = Serial.readString();
      Serial.println(str);
  }
}
