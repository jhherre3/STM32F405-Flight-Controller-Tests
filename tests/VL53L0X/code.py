import time
import board
import busio
from adafruit_vl53l0x import VL53L0X

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize VL53L0X
tof = VL53L0X(i2c)

print("VL53L0X Initialized. Starting distance measurements...")

while True:
    # Read distance in millimeters
    distance = tof.range

    # Print the distance
    print(f"Distance: {distance} mm")

    # Delay for readability
    time.sleep(1)
