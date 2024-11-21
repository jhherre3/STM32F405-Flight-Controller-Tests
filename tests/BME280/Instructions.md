# BME280 Sensor Test with STM32F405

This guide explains how to set up the BME280 sensor with the STM32F405 board and run a CircuitPython script to read temperature, pressure, and humidity data.

---

## **Required Files**
Download the required files from the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries) and place them in the `lib` folder on your `CIRCUITPY` drive:

1. **`adafruit_bus_device`** (folder)
   - Handles I2C communication.
2. **`adafruit_bme280`** (folder)
   - Contains the driver for the BME280 sensor.
3. **`adafruit_bme680.mpy`** (optional, ignore if you're only using the BME280).
   - This file is unrelated to the BME280 and can be removed or ignored for this test.

---

## **Connections**
Connect the BME280 sensor to the STM32F405 board as follows:

| **BME280 Pin** | **STM32F405 Pin**       | **Description**              |
|----------------|-------------------------|------------------------------|
| **VIN**        | 3.3V                    | Power supply for the sensor. |
| **GND**        | GND                     | Ground connection.           |
| **SCL**        | SCL                     | I2C clock line.              |
| **SDA**        | SDA                     | I2C data line.               |

---

## **Setup Steps**
1. **Prepare the CircuitPython Libraries:**
   - Copy the `adafruit_bus_device` folder and the `adafruit_bme280` folder to the `lib` directory on your `CIRCUITPY` drive.

2. **Write the Script:**
   - Save the updated test script as `code.py` on your `CIRCUITPY` drive.

3. **Monitor Serial Output:**
   - Use a serial terminal (e.g., PuTTY) to connect to the STM32F405 at **115200 baud rate**.
   - The output will display the temperature (Celsius and Fahrenheit), humidity, pressure, and calculated altitude.

---
