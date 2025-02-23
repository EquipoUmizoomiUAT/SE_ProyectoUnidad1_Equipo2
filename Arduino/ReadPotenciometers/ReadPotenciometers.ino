void setup() 
{
    Serial.begin(9600);
}

int sensorValues[6];
void loop() 
{
    for (int i = 0; i < 6; i++) 
    {
        sensorValues[i] = analogRead(A0 + i);
    }

    String reading = String(sensorValues[0]) + "," + String(sensorValues[1]) + "," + String(sensorValues[2]) + "," +
                     String(sensorValues[3]) + "," + String(sensorValues[4]) + "," + String(sensorValues[5]);

    Serial.println(reading);

    delay(100);
}