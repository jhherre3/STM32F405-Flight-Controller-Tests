# Instructions: Interpreting GPS Output

This document explains how to interpret GPS data output from your module, focusing on common NMEA sentences. An example output is included with a detailed explanation of its fields.

---

## **How to Interpret GPS Output**

### **1. NMEA Sentences Overview**

GPS modules send data as standardized **NMEA sentences**, each containing specific information:
- **`$GPGGA`**: Provides positioning data like latitude, longitude, altitude, and fix quality.
- **`$GPRMC`**: Contains position, time, and motion-related data.
- **`$GPGSV`**: Reports satellite visibility and signal strength.
- **`$GPVTG`**: Displays speed and course over the ground.

---

## **Example GPS Output**

Below is an example of raw GPS output from the module:

```plaintext
$GPGGA,060251.00,3327.79272,N,11140.88828,W,1,06,2.43,470.0,M,-27.5,M,,*66
$GPRMC,060240.00,A,3327.79289,N,11140.89037,W,0.0,60239.00,A,*71
$GPGSV,3,1,11,05,45,162,21,06,17,047,,11,57,033,26,12,77,185,19*7C
$GPVTG,T,M,0.391,N,0.724,K,A*29
