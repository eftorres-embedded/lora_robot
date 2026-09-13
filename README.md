# LoRa Robot

A Raspberry Pi Pico-based robot controlled over long-range LoRa radio using MicroPython.

This project is currently under development. The initial work focuses on establishing reliable communication between the Raspberry Pi Pico and an SX1262 LoRa transceiver before integrating the radio system with the robot's motor controls and other hardware.

## Project Goals

The goal of this project is to create a remotely controlled robot capable of communicating over LoRa for greater range than conventional Bluetooth or Wi-Fi control.

Planned capabilities include:

- Long-range LoRa communication
- Raspberry Pi Pico / MicroPython control
- Wireless transmission of robot commands
- Motor control
- Bidirectional communication
- Telemetry from the robot
- Modular hardware and software design

## Hardware

Current hardware includes:

- Raspberry Pi Pico
- SX1262 LoRa transceiver
- LoRa antenna
- Breadboard / prototype wiring

Additional robot hardware will be documented as it is added.

## Software

The project uses:

- MicroPython
- Raspberry Pi Pico
- SPI communication
- SX1262 LoRa radio
- Visual Studio Code
- MicroPico VS Code extension

## Current Project Structure

```text
lora_robot/
├── README.md
├── .gitignore
├── board_pins.py
├── sx1262_basic.py
└── test_lora.py
```

### `board_pins.py`

Defines the Raspberry Pi Pico GPIO connections used by the LoRa hardware.

### `sx1262_basic.py`

Contains the basic SX1262 driver and communication functions.

### `test_lora.py`

Test program used to verify communication between the Raspberry Pi Pico and the SX1262 LoRa module.


## LoRa Communication

The SX1262 communicates with the Raspberry Pi Pico using SPI.

The radio interface requires connections for signals such as:

- SPI clock
- MOSI
- MISO
- Chip select
- Reset
- BUSY
- DIO interrupt

The exact GPIO assignments are defined in `board_pins.py`.

## Planned Architecture

The system will eventually consist of two primary devices:

```text
Controller
    |
    |  LoRa
    |
    v
Robot
    |
    +-- Raspberry Pi Pico
    +-- SX1262 LoRa Radio
    +-- Motor Controller
    +-- Motors
    +-- Sensors / Telemetry
```

The controller will transmit commands to the robot, while the robot will be able to return status and telemetry information.

## Future Development

Future improvements may include:

- Joystick-based remote controller
- Packet acknowledgements
- Communication timeout / failsafe
- Battery voltage telemetry
- Signal strength reporting
- GPS integration
- Sensor telemetry
- Configurable LoRa parameters
- Error detection
- Motor speed control
- Autonomous operation modes

## SX1262 Wiring

The exact GPIO assignments should be taken from `board_pins.py` and verified against the physical wiring before being documented here.

| SX1262 | Raspberry Pi Pico | Function |
|---|---|---|
| VCC | TBD | Power |
| GND | GND | Ground |
| SCK | TBD | SPI Clock |
| MOSI | TBD | SPI TX |
| MISO | TBD | SPI RX |
| NSS | TBD | Chip Select |
| RESET | TBD | Reset |
| BUSY | TBD | Radio Busy |
| DIO1 | TBD | Interrupt |

## Author

**Eder F. Torres**

Embedded systems, microcontrollers, FPGA, and robotics projects.

GitHub: https://github.com/eftorres-embedded

## License

A license has not yet been selected for this project.