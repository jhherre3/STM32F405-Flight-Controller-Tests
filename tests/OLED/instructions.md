# Instructions: Setting Up an OLED Display for UAV Applications

## Overview

This guide explains how to set up a 128x64 OLED display with an STM32 microcontroller running CircuitPython. The display will show UAV telemetry data such as altitude, speed, GPS coordinates, battery level, and operational status.

---

## Prerequisites

### Hardware
1. **128x64 OLED Display** (I2C, SSD1306 driver).
2. **STM32F405 Feather Board**.
3. Jumper wires for connections.

### Software
1. CircuitPython installed on the STM32F405.
2. Required CircuitPython libraries added to the `lib` folder:
   - `adafruit_displayio_ssd1306.mpy`
   - `adafruit_display_text` folder (contains necessary text display libraries).
   - `adafruit_display_shapes.mpy` (for drawing basic shapes, if needed).
   - `adafruit_bus_device` (for I2C communication).

   Download the latest [CircuitPython Library Bundle](https://circuitpython.org/libraries).

---

## Wiring

| **OLED Pin** | **STM32 Pin** | **Description**        |
|--------------|---------------|------------------------|
| VCC          | 3.3V          | Power the OLED.        |
| GND          | GND           | Ground connection.     |
| SCL          | D1 (SCL)      | I2C clock line.        |
| SDA          | D0 (SDA)      | I2C data line.         |

---

## Steps to Deploy Code

### Step 1: Install Required Libraries
- Copy the following libraries and files into the `lib` folder on the STM32F405 drive:
  - `adafruit_displayio_ssd1306.mpy`
  - The `adafruit_display_text` folder (make sure the entire folder is included).
  - `adafruit_display_shapes.mpy`
  - `adafruit_bus_device.mpy`

### Step 2: Run code.py
