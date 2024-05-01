#include <DHT.h>  //libreria

#define SENSOR_TIPO DHT11   //especificar el tipo de sensor
#define PIN_DATOS_SENSOR 4  //PIN de datos del sensor

DHT sensor(PIN_DATOS_SENSOR, SENSOR_TIPO);

void setup() {
  Serial.begin(9600);
  sensor.begin();
}

void loop() {
  delay(2000);

  float humedad = sensor.readHumidity();
  float temperatura = sensor.readTemperature();

  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.print("%     ");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print("°C");
  Serial.print("\n");
}