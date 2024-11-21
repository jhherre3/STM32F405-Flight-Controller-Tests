import time
import board
import busio

# Initialize UART for GPS
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

print("Starting GPS NMEA parser...")

def parse_gga(sentence):
    """
    Parse $GPGGA sentence to extract latitude, longitude, and fix quality.
    """
    if sentence.startswith("$GPGGA"):
        fields = sentence.split(",")
        try:
            # Latitude
            raw_lat = fields[2]
            lat_dir = fields[3]
            latitude = convert_to_decimal(raw_lat, lat_dir)

            # Longitude
            raw_lon = fields[4]
            lon_dir = fields[5]
            longitude = convert_to_decimal(raw_lon, lon_dir)

            # Fix Quality
            fix_quality = fields[6]  # 0 = Invalid, 1 = GPS fix, 2 = DGPS fix

            # Number of Satellites
            satellites_used = fields[7]

            # HDOP
            hdop = fields[8]

            # Altitude
            altitude = fields[9]

            return latitude, longitude, fix_quality, satellites_used, hdop, altitude
        except (IndexError, ValueError):
            return None, None, 0, 0, 0, 0
    return None, None, 0, 0, 0, 0

def convert_to_decimal(raw_coord, direction):
    """
    Convert raw NMEA coordinate to decimal degrees.
    """
    if not raw_coord or direction not in ("N", "S", "E", "W"):
        return None
    # Degrees are the first two digits for latitude, first three for longitude
    if direction in ("N", "S"):
        degrees = int(raw_coord[:2])
        minutes = float(raw_coord[2:])
    else:
        degrees = int(raw_coord[:3])
        minutes = float(raw_coord[3:])
    decimal = degrees + (minutes / 60)
    if direction in ("S", "W"):
        decimal = -decimal
    return decimal

while True:
    data = uart.read(128)  # Read up to 128 bytes of data
    if data:
        try:
            sentence = data.decode("ascii").strip()
            print(f"Raw NMEA: {sentence}")

            # Parse GGA sentence
            latitude, longitude, fix_quality, satellites_used, hdop, altitude = parse_gga(sentence)
            if fix_quality != 0 and latitude and longitude:
                print(f"Latitude: {latitude:.6f}, Longitude: {longitude:.6f}")
                print(f"Fix Quality: {fix_quality} (1=GPS, 2=DGPS)")
                print(f"Satellites Used: {satellites_used}")
                print(f"HDOP: {hdop}, Altitude: {altitude} meters")
        except UnicodeDecodeError:
            continue
    time.sleep(1)
