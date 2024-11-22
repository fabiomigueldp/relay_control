#define BUZZER1_PIN 2
#define BUZZER2_PIN 25

// Notas musicais (frequências em Hz)
#define NOTE_C4  262
#define NOTE_E4  330
#define NOTE_G4  392
#define NOTE_A4  440

// Duração das notas
#define WHOLE_NOTE 1000
#define HALF_NOTE  (WHOLE_NOTE / 2)
#define QUARTER_NOTE (WHOLE_NOTE / 4)

// Função para tocar uma nota em um pino específico
void playTone(int pin, int frequency, int duration) {
  ledcAttachPin(pin, 0);  // Conecta o pino ao canal PWM
  ledcWriteTone(0, frequency);  // Toca a nota
  delay(duration);  // Espera a duração da nota
  ledcWriteTone(0, 0);  // Para de tocar
}

void playChord(int freq1, int freq2, int duration) {
  // Toca dois tons simultaneamente (acorde)
  ledcAttachPin(BUZZER1_PIN, 0);
  ledcAttachPin(BUZZER2_PIN, 1);
  ledcWriteTone(0, freq1);  // Toca a primeira nota no primeiro buzzer
  ledcWriteTone(1, freq2);  // Toca a segunda nota no segundo buzzer
  delay(duration);
  ledcWriteTone(0, 0);  // Para o primeiro buzzer
  ledcWriteTone(1, 0);  // Para o segundo buzzer
}

void setup() {
  // Configura os canais PWM para os buzzers
  ledcSetup(0, 2000, 8);  // Canal 0, 2kHz, resolução de 8 bits
  ledcSetup(1, 2000, 8);  // Canal 1, 2kHz, resolução de 8 bits
}

void loop() {
  // Toca acordes
  playChord(NOTE_C4, NOTE_E4, QUARTER_NOTE);  // Acorde C (C e E)
  delay(200);

  playChord(NOTE_E4, NOTE_G4, QUARTER_NOTE);  // Acorde Em (E e G)
  delay(200);

  playChord(NOTE_G4, NOTE_A4, QUARTER_NOTE);  // Acorde G (G e A)
  delay(200);

  playTone(BUZZER1_PIN, NOTE_C4, QUARTER_NOTE);  // Nota simples no primeiro buzzer
  delay(200);

  playTone(BUZZER2_PIN, NOTE_G4, QUARTER_NOTE);  // Nota simples no segundo buzzer
  delay(200);

  delay(1000);  // Pausa antes de reiniciar
}
