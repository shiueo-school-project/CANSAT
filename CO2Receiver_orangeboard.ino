#include <SoftwareSerial.h>

#include <MHZ19.h>

SoftwareSerial ss(2, 3);
MHZ19 mhz( & ss);

void setup() {
  Serial.begin(115200);
  ss.begin(9600);
}

int sensorValue[2];
unsigned char sensorLen = 0;

void loop() // run over and over
{
  unsigned char idx = 0;
  MHZ19_RESULT response = mhz.retrieveData();

  if (response == MHZ19_RESULT_OK)

  {

    sensorValue[0] = mhz.getCO2();
    sensorValue[1] = mhz.getTemperature();

  } else

  {

    Serial.print(F("Error, code: "));

    Serial.println(response);

  }
  sensorLen = 0;
  for (idx = 0; idx < 2; idx++) {
    if (sensorValue[idx] < 10) sensorLen += 1;
    else if (sensorValue[idx] < 100) sensorLen += 2;
    else if (sensorValue[idx] < 1000) sensorLen += 3;
    else if (sensorValue[idx] < 10000) sensorLen += 4;
    sensorLen += 1; // for ',' 
  }

  Serial.write(0x76);
  Serial.write(0x00);
  Serial.write(0xA0); // MESSAGE 0 //
  Serial.write(sensorLen);
  for (idx = 0; idx < 2; idx++) {
    Serial.print(sensorValue[idx]);
    Serial.print(',');
  }
  Serial.println();
  delay(1);
}
