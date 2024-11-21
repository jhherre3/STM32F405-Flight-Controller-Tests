import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# Debug message for startup
print("Starting BME280 sensor test...")

# Initialize I2C
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    print("I2C initialized successfully.")
except Exception as e:
    print(f"Error initializing I2C: {e}")
    while True:
        pass  # Halt execution if I2C fails

# Function to scan I2C bus
def scan_i2c():
    print("Scanning I2C bus...")
    while not i2c.try_lock():
        pass
    addresses = [hex(addr) for addr in i2c.scan()]
    i2c.unlock()
    if addresses:
        print(f"I2C addresses found: {addresses}")
    else:
        print("No I2C devices found. Check your wiring!")
    return addresses

# Scan for devices
addresses = scan_i2c()

# Default I2C address for the BME280
BME280_ADDRESS = 0x76  # Default address
if "0x77" in addresses:
    BME280_ADDRESS = 0x77  # Adjust if the sensor is detected at 0x77

# Initialize BME280 sensor
try:
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=BME280_ADDRESS)
    print(f"BME280 detected at address: {hex(BME280_ADDRESS)}")
    bme280.sea_level_pressure = 1013.25  # hPa for Mesa, AZ
except Exception as e:
    print(f"Error initializing BME280: {e}")
    while True:
        pass  # Halt execution if the sensor initialization fails

# Main loop for reading sensor data
while True:
    try:
        # Read data from the BME280
        temperature_c = bme280.temperature
        temperature_f = temperature_c * 9 / 5 + 32  # Convert to Fahrenheit
        humidity = bme280.humidity
        pressure = bme280.pressure
        altitude = bme280.altitude  # Calculated using sea-level pressure

        # Display data
        print(f"Temperature: {temperature_c:.2f} °C / {temperature_f:.2f} °F")
        print(f"Humidity: {humidity:.2f} %")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Altitude: {altitude:.2f} meters ({altitude * 3.281:.2f} feet)")
        print("-" * 40)
    except Exception as e:
        print(f"Error reading sensor data: {e}")

    time.sleep(2)  # Wait 2 seconds between readings
