import time
import board
import busio
from adafruit_mpu6050 import MPU6050

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the MPU6050 with address 0x69 (AD0 connected to 3.3V)
mpu = MPU6050(i2c, address=0x69)

# Print a message if initialized
print("MPU6050 Initialized at address 0x69")

while True:
    # Read accelerometer data
    accel_x, accel_y, accel_z = mpu.acceleration
    # Read gyroscope data
    gyro_x, gyro_y, gyro_z = mpu.gyro
    # Read temperature
    temp = mpu.temperature

    # Print the data
    print(f"Accel (m/s^2): X={accel_x:.2f}, Y={accel_y:.2f}, Z={accel_z:.2f}")
    print(f"Gyro (rad/s): X={gyro_x:.2f}, Y={gyro_y:.2f}, Z={gyro_z:.2f}")
    print(f"Temp (C): {temp:.2f}")
    print("------")

    # Delay for readability
    time.sleep(1)
