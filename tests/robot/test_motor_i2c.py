from machine import Pin, I2C

import board_pins

i2c = I2C(
    1,
    sda=Pin(board_pins.MOTOR_SDA),
    scl=Pin(board_pins.MOTOR_SCL),
    freq=100_000
)

devices =  i2c.scan()

print("I2C devices:", devices)

for address in devices:
    print(
        "Found device:",
        address,
        "hex:",
        hex(address)
    )