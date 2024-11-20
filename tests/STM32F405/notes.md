# Setting Up CircuitPython on STM32F405

This guide explains how to flash CircuitPython firmware onto the STM32F405 board.

## Steps to Flash CircuitPython

1. **Download CircuitPython Firmware**
   - Visit the [CircuitPython STM32F405 page](https://circuitpython.org/board/feather_stm32f405_express/).
   - Download the `.bin` firmware file for your board.

2. **Prepare the STM32F405 for Flashing**
   - Put the STM32F405 into **boot mode**:
     - Hold the **BOOT0** button.
     - While holding BOOT0, press and release the **RESET** button.
     - Release BOOT0 after reset.

3. **Flash the Firmware**
   - Use a programmer to flash the `.bin` file onto the board:
     - Open your STM32 flashing tool (e.g., STM32CubeProgrammer or `dfu-util`).
     - Select the `.bin` firmware file.
     - Flash the file to the board.

4. **Verify Installation**
   - Once the flashing process is complete, the STM32F405 will reboot.
   - The board should appear as a USB drive labeled `CIRCUITPY`.

5. **Start Coding**
   - Open the `code.py` file on the `CIRCUITPY` drive and write your CircuitPython scripts.
   - For libraries, examples, and documentation, [Adafruit CircuitPython site](https://learn.adafruit.com/welcome-to-circuitpython).

---

Follow these steps to set up CircuitPython and start working with your STM32F405 board!
