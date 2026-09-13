from machine import Pin, SPI
from time import sleep_ms, ticks_ms, ticks_diff

import board_pins

class SX1262Basic:
    def __init__(self):
        self.cs = Pin(
            board_pins.LORA_CS,
            Pin.OUT
        )

        self.cs.value(1)

        self.reset_pin = Pin(
            board_pins.LORA_RESET,
            Pin.OUT
        )

        self.reset_pin.value(1)

        self.busy = Pin(
            board_pins.LORA_BUSY,
            Pin.IN
        )

        self.dio1 = Pin(
            board_pins.LORA_DIO1,
            Pin.IN
        )

        self.spi = SPI(
            1,
            baudrate=1_000_000,
            polarity=0,
            phase=0,
            sck=Pin(board_pins.LORA_SCK),
            mosi=Pin(board_pins.LORA_MOSI),
            miso=Pin(board_pins.LORA_MISO)
        )

    def read_busy(self):
        return self.busy.value()

    def read_dio1(self):
        return self.dio1.value()

    def wait_while_busy(self, timeout_ms=1000):
        start = ticks_ms()
        while self.busy.value():
            if ticks_diff(ticks_ms(), start) > timeout_ms:
                raise RuntimeError("SX1262 Busy timeout")

    def reset(self):
        print("Resetting SX1262...")
        self.reset_pin.value(0)
        sleep_ms(1)
        self.reset_pin.value(1)
        #Giving Radio some time
        sleep_ms(10)
        self.wait_while_busy()
        print("Reset complete.")

    def get_status(self):
        self.wait_while_busy()

        tx = bytes([0xC0, 0x00])
        rx = bytearray(2)

        self.cs.value(0)

        self.spi.write_readinto(tx,rx)

        self.cs.value(1)

        self.wait_while_busy()

        return rx[1]
