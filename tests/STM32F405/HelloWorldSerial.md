# Hello World: Serial Communication with STM32F405 Using CircuitPython

This tutorial demonstrates how to set up and test serial communication on the STM32F405 board using CircuitPython. We'll write a "Hello World" program, set up the baud rate to 115200, and monitor the output using PuTTY.

---

## Prerequisites

1. **STM32F405 Board** with CircuitPython installed.
2. **PuTTY** or another serial terminal application (e.g., Mu Editor, minicom).
3. **PyCharm (optional)** or any text editor for editing `code.py`.

---

## Step 1: Write the `code.py` Script

1. Open the `CIRCUITPY` drive on your computer.
2. Edit the `code.py` file (or create one if it doesn’t exist).
3. Paste the following script into `code.py`:

```python
import time

# Send a message repeatedly over the serial connection
while True:
    print("Hello from STM32F405!")
    time.sleep(1)  # Wait 1 second between messages
