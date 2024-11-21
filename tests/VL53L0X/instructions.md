# Instructions: Setting Up and Using the VL53L0X Sensor

This document provides step-by-step instructions for wiring, library setup, and running the VL53L0X sensor with your STM32F405 Express board using CircuitPython.

---

## **1. Wiring the VL53L0X**

Connect the VL53L0X to your STM32F405 as follows:

| **VL53L0X Pin** | **STM32 Pin**       | **Description**                   |
|------------------|---------------------|------------------------------------|
| VIN              | 3.3V               | Power the sensor.                  |
| GND              | GND                | Ground connection.                 |
| SCL              | D1 (SCL)           | I2C clock line.                    |
| SDA              | D0 (SDA)           | I2C data line.                     |
| XSHUT            | Not Connected (Optional) | Shutdown pin for multiple sensors. |

### **Important Note**
If using multiple VL53L0X sensors on the same I2C bus, connect the **XSHUT** pin of each sensor to a unique GPIO pin on the STM32 board. This allows each sensor to be initialized with a unique I2C address.

---

## **2. Required Libraries**

### **Libraries Needed**
1. `adafruit_bus_device`: For I2C communication.
2. `adafruit_vl53l0x.mpy`: Driver for VL53L0X.

### **Installing Libraries**
1. Download the latest [CircuitPython Bundle](https://circuitpython.org/libraries).
2. Copy the following files to the `lib` folder on your STM32 board:
   - `adafruit_bus_device`
   - `adafruit_vl53l0x.mpy`

---

## **3. Run code.py**
