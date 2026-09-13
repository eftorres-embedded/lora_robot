# board_pins.py
#
# Raspberry Pi Pico pin assigments
# Lora Robot Project


# Waveshare Pico-LoRa-SX1262 pin assignments

LORA_BUSY = 2
LORA_CS = 3

LORA_SCK = 10
LORA_MOSI = 11
LORA_MISO = 12

LORA_RESET = 15
LORA_DIO1 = 20

BATTERY_ADC = 26

# Waveshare Pico Motor Driver
# I2C jumpers moved to GP6/GP7
MOTOR_SDA = 6
MOTOR_SCL = 7