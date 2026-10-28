/*
 * Experiment 16 / 17: Ultrasonic Distance Measurement using Arduino Development Board
 */
const int trigPin = 6;
const int echoPin = 7;

long duration;
int distance;

void setup()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Distance in cm: ");
  Serial.println(distance);

  delay(2000);
}
