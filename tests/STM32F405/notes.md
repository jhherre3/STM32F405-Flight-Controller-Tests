# Setting Up CircuitPython on STM32F405

This guide explains how to flash CircuitPython firmware onto the STM32F405 board.

## Steps to Flash CircuitPython

1. **Download CircuitPython Firmware**
   - Visit the [CircuitPython STM32F405 page](https://circuitpython.org/board/feather_stm32f405_express/).
   - Download the `.bin` firmware file for your board.

2. **Prepare the STM32F405 for Flashing**
   - Put the STM32F405 into **boot mode**:
     - Jump from pad **3.3v --to-- BO**.
     - Press and release the **RESET** button.
     - In DFU mode

3. **Flash the Firmware**
   - Use a STM programmer to flash the `.bin` file onto the board:
     - Open your STM32 flashing tool (STM32CubeProgrammer).
     - While in DFU mode connect via USB connection
     - In software under USB config refresh port
     - connect to stm
     - Under erase & programming upload file
     - Select the `.bin` firmware file.
     - Flash the file to the board.

4. **Verify Installation**
   - Once the flashing process is complete, the STM32F405 will reboot.
   - The board should appear as a USB drive labeled `CIRCUITPY`.

5. **Start Coding**
   - Open the `code.py` file on the `CIRCUITPY` drive and write your CircuitPython scripts.
   - For libraries, examples, and documentation, [Adafruit CircuitPython site](https://learn.adafruit.com/welcome-to-circuitpython).

---
