#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

const double wait = 25; // in ms
int bit_pins[] = {0, 1, 2, 3, 4, 5, 6, 7}; //TODO: Fill with real RasPi pins
int data_pin = 17;

void wait_for(double seconds) {
  clock_t start = clock() / (CLOCKS_PER_SEC / 1000);

  clock_t current_time = start; 
  while (current_time <= start + seconds) {
    current_time = clock() / (CLOCKS_PER_SEC / 1000);
  } 
}

void setup_pin(int pin_number) {
  char init_cmd[80];
  sprintf(init_cmd, "echo %d > /sys/class/gpio/export", pin_number);
  system(init_cmd);

  char direction_cmd[80];
  sprintf(direction_cmd, "echo out > /sys/class/gpio/gpio%d/direction", pin_number);
  system(direction_cmd);
}

void setup() {
  for (int i = 0; i < 8; i++) {
    setup_pin(i);
  }

  setup_pin(data_pin);
}

void cleanup() {
  for (int i = 0; i < 8; i++) {
    char clean_cmd[80];
    sprintf(clean_cmd, "echo %d > /sys/class/gpio/unexport", i);
    system(clean_cmd);
  }
}

void write(int pin_number, int output) {
  char write_cmd[80];
  sprintf(write_cmd, "echo %d > /sys/class/gpio/gpio%d/value", output, pin_number);
  system(write_cmd);

}

void clear_pins() {
  for (int i = 0; i < 8; i++) {
    write(bit_pins[i], 0);
  }

  write(data_pin, 0);
}

void light_bit_pin(int bit_number) {
  write(bit_pins[bit_number], 1);

  printf("Bit pin %d lit\n", bit_pins[bit_number]);
}

void light_data_pin() {
  write(data_pin, 1);

  printf("Data pin lit\n");
}

// data = 1 byte of data
void send(int data) {
  if (data > 256) { // Data larger than 1 byte
    printf("send method given data larger than 1 byte. Aborting...\n");
    exit(0); //TODO: Use a proper error number
  }

  clear_pins();
  for (int i = 0; i < 8; i++) {
    if ((data & (0x01 << i)) > 0) {
      light_bit_pin(i);
    }
  }

  light_data_pin(); 
  wait_for(wait);
  printf("Clearing pins\n");
  clear_pins();
  wait_for(wait);
}

extern "C" {
	void lib_waitFor(double seconds) { wait_for(seconds); }
	void lib_setupPin(int pin) { setup_pin(pin); }
	void lib_setup() { setup(); }
	void lib_cleanup() { cleanup(); }
	void lib_write(int pina, int pinb) { write(pina, pinb); }
	void lib_clearPins() { clear_pins(); }
	void lib_lightBitPin(int bitn) { light_bit_pin(bitn); }
	void lib_lightDataPin() { light_data_pin(); }
    void lib_send(int i){ send(i); }
}
