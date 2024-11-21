import board
import displayio
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_display_shapes.rect import Rect
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

# Add a rectangle to the group
rectangle = Rect(x=10, y=10, width=50, height=30, fill=0xFFFFFF)  # A white rectangle
group.append(rectangle)

# Add a text label to the group
hello_label = label.Label(terminalio.FONT, text="Hello World!", color=0xFFFFFF, x=10, y=50)
group.append(hello_label)

# Set the display's root group to show the content
oled.root_group = group

print("Displayed 'Hello World!' and a rectangle on the OLED!")

# Loop forever
while True:
    pass
