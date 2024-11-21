# Instructions: Setting Up the MPU6050 with STM32 and CircuitPython

This document provides step-by-step instructions for wiring the MPU6050, setting the I2C address via the AD0 pin, using the `6050.mpy` library, and understanding the code's mathematical operations.

---

## **1. Wiring the MPU6050 to STM32**

### **Pin Connections**
The MPU6050 uses the I2C protocol for communication. Connect it to your STM32F405 Express board as follows:

| **MPU6050 Pin** | **STM32 Pin**       | **Description**                |
|------------------|---------------------|---------------------------------|
| VCC              | 3.3V               | Power supply for the MPU6050.   |
| GND              | GND                | Ground connection.              |
| SCL              | D1 (SCL)           | I2C clock line.                 |
| SDA              | D0 (SDA)           | I2C data line.                  |
| AD0              | 3.3V               | Sets the I2C address to `0x69`. |

### **Important Note: AD0 and I2C Address**
- Connecting **AD0 to GND** sets the I2C address to **`0x68`**.
- Connecting **AD0 to 3.3V** sets the I2C address to **`0x69`**.
- Ensure the code matches the selected address. For this setup, **AD0 is connected to 3.3V**, so the I2C address is `0x69`.

---

## **2. Required Libraries**

1. **`adafruit_bus_device`**: Handles I2C communication.
2. **`adafruit_mpu6050.mpy`**: Driver for the MPU6050.

### **Installing Libraries**
- Download the latest [CircuitPython Bundle](https://circuitpython.org/libraries).
- Copy the following files to the `lib` folder of your STM32:
  - `adafruit_bus_device`
  - `adafruit_mpu6050.mpy`

---

## **3. Code Overview**

### **Main Code**
The code initializes the MPU6050, reads data (acceleration, gyroscope, and temperature), and prints it to the console. Here is the critical part of the initialization:

```python
i2c = busio.I2C(board.SCL, board.SDA)
mpu = MPU6050(i2c, address=0x69)
