import time
import board
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_text import label
import terminalio

# Release any previously configured displays
displayio.release_displays()

# Initialize I2C
i2c = board.I2C()  # Uses board.SCL and board.SDA

# Set up the OLED display
WIDTH = 128
HEIGHT = 64  # Adjust for 128x64 OLED
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
oled = SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Create a display group
group = displayio.Group()

# Create labels for telemetry data with adjusted row positions
altitude_label = label.Label(terminalio.FONT, text="Altitude: 0.0m", color=0xFFFFFF, x=0, y=10)
speed_label = label.Label(terminalio.FONT, text="Speed: 0.0m/s", color=0xFFFFFF, x=0, y=20)
gps_label = label.Label(terminalio.FONT, text="GPS: N/A", color=0xFFFFFF, x=0, y=30)
battery_label = label.Label(terminalio.FONT, text="Battery: 100%", color=0xFFFFFF, x=0, y=40)
status_label = label.Label(terminalio.FONT, text="Status: Disarmed", color=0xFFFFFF, x=0, y=50)

# Add the labels to the group
group.append(altitude_label)
group.append(speed_label)
group.append(gps_label)
group.append(battery_label)
group.append(status_label)

# Set the display's root group
oled.root_group = group

# Simulated data for testing
altitude = 0.0
speed = 0.0
gps_coords = "33.4631N, 111.6812W"
battery = 100
status = "Disarmed"  # Default status

# Update display in a loop
while True:
    # Simulate telemetry updates
    altitude += 0.1
    speed += 0.05
    battery -= 0.01
    if battery < 20:
        status = "Low Battery!"
    elif battery <= 0:
        status = "Critical!"
    else:
        status = "Disarmed"  # Ensure status reflects disarmed when no warnings apply

    # Update labels
    altitude_label.text = f"Altitude: {altitude:.1f}m"
    speed_label.text = f"Speed: {speed:.1f}m/s"
    gps_label.text = f"GPS: {gps_coords}"
    battery_label.text = f"Battery: {battery:.0f}%"
    status_label.text = f"Status: {status}"

    # Pause to simulate real-time updates
    time.sleep(0.5)
