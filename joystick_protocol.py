from ctypes import cdll
lib = cdll.LoadLibrary('./JoystickProtocol.so')

def wait_for(seconds):
	lib.lib_waitFor(seconds)

def setup_pin(pin_num):
	lib.lib_setupPin(pin)

def setup():
	lib.lib_setup()

def cleanup():
	lib.lib_cleanup()

def write(pin_num, value):
	lib.lib_write(pin_num, value)

def clear_pins():
	lib.lib_clearPins()

def light_bit_pin(bit_number):
	lib.lib_lightBitPin()

def light_data_pin():
	lib.lib_lightDataPin()

def send(data):
	lib.lib_send(data)
