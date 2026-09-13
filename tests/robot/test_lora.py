from machine import ADC
from firmware.robot.drivers.sx1262 import SX1262
from firmware.robot.board_pins import BATTERY_ADC
from machine import Pin, I2C

i2c = I2C(
    1,
    sda=Pin(6),
    scl=Pin(7),
    freq=400_000
)


print()
print("==============================")
print("SX1262 BASIC HARDWARE TEST")
print("==============================")
print()


# -------------------------
# Create radio interface
# -------------------------

radio = SX1262()

print("Initial BUSY:", radio.read_busy())
print("Initial DIO1:", radio.read_dio1())
print()


# -------------------------
# Reset radio
# -------------------------

radio.reset()

print("BUSY after reset:", radio.read_busy())
print("DIO1 after reset:", radio.read_dio1())
print()


# -------------------------
# Test SPI communication
# -------------------------

print("Reading SX1262 status...")

sx1262_status = radio.get_status()
print("Raw sx1262 status:", sx1262_status)
print("Raw sx1262 status hex:", hex(sx1262_status))

print()


# -------------------------
# Read battery ADC
# -------------------------

battery = ADC(BATTERY_ADC)

raw = battery.read_u16()

print("Battery ADC raw:", raw)


devices = i2c.scan()

print(devices)

for device in devices:
    print(hex(device))

print()
print("==============================")
print("TEST COMPLETE")
print("==============================")