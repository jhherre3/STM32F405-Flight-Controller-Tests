# LIS3MDL Magnetometer Background and Instructions

## Overview
The **LIS3MDL** is a high-performance, three-axis magnetometer sensor designed for applications requiring accurate magnetic field measurements. It is widely used in drones and Unmanned Aerial Systems (UAS) for navigation, stability, and orientation sensing. The sensor operates via I2C or SPI interfaces and offers high sensitivity with low power consumption, making it ideal for embedded systems.
 
---

## Key Features
- **Three-axis Magnetometer**: Measures magnetic fields in X, Y, and Z directions.
- **Sensitivity Range**: Configurable from ±4 gauss to ±16 gauss.
- **Communication Protocols**: Supports I2C and SPI for flexible interfacing.
- **Low Power Consumption**: Ideal for battery-operated devices like drones.
- **High Accuracy**: Provides reliable data even in the presence of environmental noise.

---

## Libraries Required
To work with the LIS3MDL magnetometer using CircuitPython, the following libraries must be installed:

1. **Adafruit LIS3MDL**: 
   - Provides easy access to the LIS3MDL sensor's functionality.
   - File: `adafruit_lis3mdl.mpy` and folder

2. **Adafruit Bus Device**:
   - Required for I2C communication.
   - File: `adafruit_bus_device`

3. **Adafruit Register**:
   - Used for handling sensor registers.
   - File: `adafruit_register`

### Installation
1. Download the latest [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries).
2. Copy the above `.mpy` files and folders into the `lib/` directory on the `CIRCUITPY` drive of your board.

---

## Wiring Instructions
Connect the LIS3MDL magnetometer to the STM32F405 board as follows:

| **LIS3MDL Pin** | **STM32F405 Pin**      | **Description**            |
|------------------|------------------------|----------------------------|
| VIN             | 3.3V or 5V            | Power supply for the sensor |
| GND             | GND                   | Ground connection          |
| SCL             | SCL                   | I2C Clock                  |
| SDA             | SDA                   | I2C Data                   |

### Notes:
- Ensure the LIS3MDL module supports the selected voltage (3.3V or 5V).

---

## Usage in Drones and UAS
1. **Magnetic Heading Calculation**:
   - The LIS3MDL is used as an electronic compass to determine the drone’s heading relative to the Earth's magnetic field. This is essential for navigation, waypoint tracking, and orientation stabilization.
   
2. **Yaw Control**:
   - Combined with other sensors like gyroscopes and accelerometers, the magnetometer helps maintain precise yaw control by detecting deviations from the intended direction.

3. **Autonomous Navigation**:
   - For autonomous drones, the magnetometer aids in GPS-denied environments by offering orientation information that complements inertial measurements.

---
