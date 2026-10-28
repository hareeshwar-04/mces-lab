/*
 * Experiment 14 / 15: Buzzer Interfacing using Arduino Development Board
 */
const int BUZZER_PIN = 8;

void setup()
{
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop()
{
  digitalWrite(BUZZER_PIN, HIGH);
  delay(1000);
  digitalWrite(BUZZER_PIN, LOW);
  delay(1000);
}
