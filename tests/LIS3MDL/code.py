import board
import busio
import time
from adafruit_lis3mdl import LIS3MDL

# Initialize I2C bus
try:
    i2c = busio.I2C(board.SCL, board.SDA)
except Exception as e:
    print(f"Failed to initialize I2C: {e}")
    while True:
        pass

# Initialize LIS3MDL sensor
try:
    sensor = LIS3MDL(i2c)
    print("LIS3MDL Magnetometer Initialized")
except Exception as e:
    print(f"Failed to initialize LIS3MDL: {e}")
    while True:
        pass

# Calibration offsets (adjust as needed)
offset_x = 0.0
offset_y = 0.0
offset_z = 0.0

while True:
    try:
        # Read raw magnetic field data
        mag_x, mag_y, mag_z = sensor.magnetic

        # Apply calibration offsets
        cal_x = mag_x - offset_x
        cal_y = mag_y - offset_y
        cal_z = mag_z - offset_z

        # Print magnetic field data
        print(f"Raw Magnetic Field (uT): X={mag_x:.2f}, Y={mag_y:.2f}, Z={mag_z:.2f}")
        print(f"Calibrated Magnetic Field (uT): X={cal_x:.2f}, Y={cal_y:.2f}, Z={cal_z:.2f}")

    except Exception as e:
        print(f"Error reading sensor: {e}")

    time.sleep(0.5)
