#include <stdio.h>
#include "encode.h"

int main() {
  setup();
  for (int i = 0; i <= 256; i++) {
    send(i);
  }
  cleanup();
  return 0;
}
