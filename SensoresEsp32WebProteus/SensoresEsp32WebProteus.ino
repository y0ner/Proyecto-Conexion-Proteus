//Incluimos las librerias para el sensor de temperatura LM75
#include <inttypes.h>
#include <Wire.h>
#include <lm75.h>
//Incluimos la libreria para el sensor de temperatura y humedad DHT11
#include <DHT11.h>

// Inicializamos el sensor LM75 de Temperatura con el objeto TempI2C_LM75
TempI2C_LM75 TemperaturaLM75 = TempI2C_LM75(0x48, TempI2C_LM75::nine_bits);
//Inicializamos el sensor DHT con el objeto DHT11
DHT11 DatoS1(6);
DHT11 DatoS2(7);
DHT11 DatoS3(8);

void setup()
{
  Serial.begin(9600);  // Inicializamos el puerto serial
  Serial.println("Start");
  Serial.println("Actual temp: ");
  //Los pines 19 y 18 leen el valor del sensor mediante el metodo getTemp()
  // Serial.print(TemperaturaLM75.getTemp()); // Utiliza el objeto TemperaturaLM75 para obtener la temperatura
  // Serial.println(" ºC");
  delay(1000);
}

void loop()
{
  float tempDHT1 = DatoS1.readTemperature(); // Lee la temperatura del sensor DHT11
  float hum1 = DatoS1.readHumidity(); // Lee la humedad del sensor DHT11
  float tempDHT2 = DatoS2.readTemperature(); 
  float hum2 = DatoS2.readHumidity();
  float tempDHT3 = DatoS3.readTemperature(); 
  float hum3 = DatoS3.readHumidity(); 
  float lm75 = TemperaturaLM75.getTemp();

  Serial.print(tempDHT1);
  Serial.print(",");
  Serial.print(hum1);
  Serial.print(",");
  Serial.print(tempDHT2);
  Serial.print(",");
  Serial.print(hum2);
  Serial.print(",");
  Serial.print(tempDHT3);
  Serial.print(",");
  Serial.print(hum3);
  Serial.print(",");
  Serial.print(lm75);
  /*
  //Imprimimos la temperatura y la humedad del sensor DHT11 Primero
  Serial.print("Temp DHT11: ");
  Serial.print(tempDHT1);
  Serial.println("ºC");
  Serial.print("Humedad DHT11: ");
  Serial.print(hum1);
  Serial.println("%");
  
  //Imprimimos la temperatura y la humedad del sensor DHT11 segundo
  Serial.print("Temp DHT11: ");
  Serial.print(tempDHT2);
  Serial.println("ºC");
  Serial.print("Humedad DHT11: ");
  Serial.print(hum2);
  Serial.println("%");

  //Imprimimos la temperatura y la humedad del sensor DHT11 tercero
  Serial.print("Temp DHT11: ");
  Serial.print(tempDHT3);
  Serial.println("ºC");
  Serial.print("Humedad DHT11: ");
  Serial.print(hum3);
  Serial.println("%");

  //Imprimimos la temperatura del sensor LM75 
  Serial.print("Temp LM75: ");
  Serial.print(TemperaturaLM75.getTemp()); // Utiliza el objeto TemperaturaLM75 para obtener la temperatura
  Serial.println(" ºC");*/

  
  delay(1000);
}
