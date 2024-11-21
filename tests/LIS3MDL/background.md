# LIS3MDL Magnetometer Background

## Overview
The **LIS3MDL** is a high-performance, three-axis magnetometer sensor designed for applications requiring accurate magnetic field measurements. It is widely used in drones and Unmanned Aerial Systems (UAS) for navigation, stability, and orientation sensing. The sensor operates via I2C or SPI interfaces and offers high sensitivity with low power consumption, making it ideal for embedded systems.

---

## Key Features
- **Three-axis Magnetometer**: Measures magnetic fields in X, Y, and Z directions.
- **Sensitivity Range**: Configurable from ±4 gauss to ±16 gauss.
- **Communication Protocols**: Supports I2C and SPI for flexible interfacing.
- **Low Power Consumption**: Ideal for battery-operated devices like drones.
- **High Accuracy**: Provides reliable data even in the presence of environmental noise.

---

## Applications in Drones and UAS
1. **Magnetic Heading Calculation**:
   - The LIS3MDL is used as an electronic compass to determine the drone’s heading relative to the Earth's magnetic field. This is essential for navigation, waypoint tracking, and orientation stabilization.
   
2. **Yaw Control**:
   - Combined with other sensors like gyroscopes and accelerometers, the magnetometer helps maintain precise yaw control by detecting deviations from the intended direction.

3. **Autonomous Navigation**:
   - For autonomous drones, the magnetometer aids in GPS-denied environments by offering orientation information that complements inertial measurements.

4. **Magnetic Field Mapping**:
   - The sensor can be used for geophysical surveys and mapping magnetic anomalies, providing valuable data for industrial and environmental applications.

---

## Calculations Used
The LIS3MDL provides raw magnetic field readings in microteslas (µT) for the X, Y, and Z axes. These values are processed for drone applications as follows:

### 1. Magnetic Heading Calculation
The magnetic heading (yaw) is calculated using the arctangent function:

```math
Heading (degrees) = arctan2(Y, X) × (180 / π)
