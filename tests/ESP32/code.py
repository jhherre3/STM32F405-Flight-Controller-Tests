import time
import board
import pwmio
import busio
from digitalio import DigitalInOut, Direction

# Initialize UART on STM32 (e.g., D1 for TX, D0 for RX)
uart = busio.UART(board.TX, board.RX, baudrate=9600)

# Initialize the onboard LED
led = DigitalInOut(board.LED)  # Replace `board.LED` with the correct pin for your STM32
led.direction = Direction.OUTPUT

print("STM32 UART Transmitter with LED Blink")

while True:
    # Message to send
    message = "Hello from STM32\n"
    uart.write(message.encode("utf-8"))
    print(f"Sent: {message.strip()}")

    # Blink the LED
    led.value = True  # Turn LED on
    time.sleep(0.5)
    led.value = False  # Turn LED off
    time.sleep(1.5)  # Wait for the remaining time (total 2 seconds)
