import time
import math
import board
import busio
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label
from adafruit_mpu6050 import MPU6050
from adafruit_lis3mdl import LIS3MDL
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_gps
import terminalio

# Initialize I2C for sensors
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize UART for GPS
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

# Initialize MPU6050
mpu = MPU6050(i2c, address=0x69)

# Initialize LIS3MDL (Compass)
lis3mdl = LIS3MDL(i2c)

# Initialize BMP280 (Environmental)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
bme280.sea_level_pressure = 1013.25  # Update for your location

# Configure GPS
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")  # Update rate: 1 Hz

# Initialize OLED display (Flipped 180 degrees)
WIDTH = 128
HEIGHT = 64
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
oled = SSD1306(display_bus, width=WIDTH, height=HEIGHT, rotation=180)

# Create display group
group = displayio.Group()
title_label = label.Label(terminalio.FONT, text="Drone Data", color=0xFFFFFF, x=5, y=5)
data_label1 = label.Label(terminalio.FONT, text="--", color=0xFFFFFF, x=5, y=25)
data_label2 = label.Label(terminalio.FONT, text="--", color=0xFFFFFF, x=5, y=45)
group.append(title_label)
group.append(data_label1)
group.append(data_label2)
oled.root_group = group

# Calibration offsets for LIS3MDL
OFFSET_X = 16.75
OFFSET_Y = -39.43
MAGNETIC_DECLINATION = 11.0  # Update based on your location

# Helper functions
def calculate_heading(mag_x, mag_y):
    heading = math.atan2(mag_y, mag_x) * (180 / math.pi)
    if heading < 0:
        heading += 360
    return (heading + MAGNETIC_DECLINATION) % 360

def heading_to_cardinal(heading):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(heading / 45) % 8
    return directions[index]

def calculate_pitch_roll(accel_x, accel_y, accel_z):
    pitch = math.atan2(accel_x, math.sqrt(accel_y ** 2 + accel_z ** 2)) * (180 / math.pi)
    roll = math.atan2(accel_y, math.sqrt(accel_x ** 2 + accel_z ** 2)) * (180 / math.pi)
    return pitch, roll

# Cycle timer
cycle_start = time.monotonic()
cycle_interval = 3  # Seconds to display each subsystem's data
state = 0  # 0=Compass, 1=GPS, 2=MPU6050, 3=BMP280

# Main loop
while True:
    gps.update()  # Update GPS data

    # Collect data
    try:
        # Compass (LIS3MDL)
        raw_x, raw_y, raw_z = lis3mdl.magnetic
        calibrated_x = raw_x - OFFSET_X
        calibrated_y = raw_y - OFFSET_Y
        heading = calculate_heading(calibrated_x, calibrated_y)
        direction = heading_to_cardinal(heading)
        compass_data = f"Heading: {heading:.2f}°"
        compass_extra = f"Dir: {direction}"

        # GPS
        if gps.has_fix:
            gps_data = f"Lat: {gps.latitude:.6f}, Lon: {gps.longitude:.6f}"
            gps_extra = f"Sats: {gps.satellites}"
        else:
            gps_data = "Waiting for GPS fix..."
            gps_extra = ""

        # MPU6050
        accel_x, accel_y, accel_z = mpu.acceleration
        pitch, roll = calculate_pitch_roll(accel_x, accel_y, accel_z)
        mpu_data = f"Pitch: {pitch:.2f}°, Roll: {roll:.2f}°"

        # BMP280
        temperature = bme280.temperature
        altitude = bme280.altitude
        bmp_data = f"Temp: {temperature:.2f}°C"
        bmp_extra = f"Alt: {altitude:.2f}m"

        # Debug output to UART
        print(f"Compass: {compass_data}, {compass_extra}")
        print(f"GPS: {gps_data}, {gps_extra}")
        print(f"MPU: {mpu_data}")
        print(f"BMP: {bmp_data}, {bmp_extra}")
        print("-" * 40)

        # Update OLED display on cycle
        current_time = time.monotonic()
        if current_time - cycle_start >= cycle_interval:
            cycle_start = current_time
            state = (state + 1) % 4

            if state == 0:  # Compass
                title_label.text = "Compass"
                data_label1.text = compass_data
                data_label2.text = compass_extra
            elif state == 1:  # GPS
                title_label.text = "GPS Data"
                data_label1.text = gps_data
                data_label2.text = gps_extra
            elif state == 2:  # MPU6050
                title_label.text = "Orientation"
                data_label1.text = mpu_data.split(",")[0]
                data_label2.text = mpu_data.split(",")[1]
            elif state == 3:  # BMP280
                title_label.text = "Environment"
                data_label1.text = bmp_data
                data_label2.text = bmp_extra

    except Exception as e:
        print(f"Error: {e}")
        title_label.text = "Error"
        data_label1.text = "Check console."
        data_label2.text = ""
