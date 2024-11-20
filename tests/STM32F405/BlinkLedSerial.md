# Flashing an Onboard LED with STM32F405 Using CircuitPython

In this tutorial, we’ll create a simple script to flash the onboard LED on the STM32F405 board. This will help you understand how to control GPIO pins using CircuitPython.

---

## Prerequisites

1. **STM32F405 Board** with CircuitPython installed.
2. **PuTTY** (or any serial terminal) to monitor the status.
3. Ensure the `CIRCUITPY` drive is accessible.

---

## Required Libraries

No additional libraries are required for this example. CircuitPython’s built-in `digitalio` module is used to control the onboard LED.

---

## Step 1: Write the `code.py` Script

1. Open the `CIRCUITPY` drive on your computer.
2. Edit the `code.py` file (or create one if it doesn’t exist).
3. Paste the following script into `code.py`:

```python
import board
import digitalio
import time

# Initialize the onboard LED (replace with board.LED if using a standard pin name)
led = digitalio.DigitalInOut(board.D13)  # D13 is usually the onboard LED
led.direction = digitalio.Direction.OUTPUT

# Flash the LED in a loop
while True:
    led.value = True  # Turn LED on
    print("LED ON")
    time.sleep(0.5)  # Wait for 0.5 seconds
    led.value = False  # Turn LED off
    print("LED OFF")
    time.sleep(0.5)  # Wait for 0.5 seconds
