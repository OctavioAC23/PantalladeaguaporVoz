const int numCols = 8; // Número de columnas
int ledPins[] = {4, 5, 6, 7, 8, 9, 10, 11}; // Pines de los LEDs (pueden ser cualquier pin digital)

void setup() {
  Serial.begin(9600); // Inicializa la comunicación serial

  for (int i = 0; i < numCols; i++) {
    pinMode(ledPins[i], OUTPUT); // Configura los pines de los LEDs como salida
  }
}
void loop() {
  if (Serial.available() >= numCols) { // Espera recibir una fila completa de datos
    for (int col = 0; col < numCols; col++) {
      char received = Serial.read(); // Lee el dato recibido
      if (received == '0') {
        digitalWrite(ledPins[col], LOW); // Apaga el LED correspondiente si recibe '0'
      } else if (received == '1') {
        digitalWrite(ledPins[col], HIGH); // Enciende el LED correspondiente si recibe '1'
      }
    }
    delay(20);
    // Apaga todos los LEDs
    for (int i = 0; i < 8; i++) {
      digitalWrite(ledPins[i], LOW);
    }

  }
}

