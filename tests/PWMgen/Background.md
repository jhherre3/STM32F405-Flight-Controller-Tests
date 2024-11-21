# Background: PWM Motor Simulation on STM32

## **Introduction**

Pulse Width Modulation (PWM) is a widely used technique in motor control for drones, UAVs, and other robotics applications. It involves modulating the width of a square wave to control the amount of power delivered to a device, such as a motor or LED.

This project demonstrates how to generate a PWM signal using the STM32 microcontroller with CircuitPython. The example simulates motor control by varying the duty cycle of a PWM signal and visualizes the behavior using both serial output (Putty) and a waveform on an oscilloscope.

---

## **What is PWM?**

- **Pulse Width Modulation**:
  - PWM is a method of controlling power by switching a signal on and off at a constant frequency.
  - The proportion of time the signal stays high (the "duty cycle") determines the power output.

- **Duty Cycle**:
  - Represented as a percentage of the signal's period.
  - Example:
    - **0% Duty Cycle**: Signal stays low (motor off).
    - **50% Duty Cycle**: Signal stays high for half the period (moderate throttle).
    - **100% Duty Cycle**: Signal stays high for the entire period (full throttle).

---

## **Use Case in UAVs**

1. **Motor Control**:
   - PWM signals are sent to Electronic Speed Controllers (ESCs) to adjust motor speed.
   - The duty cycle corresponds to the throttle level for the motor.

2. **Testing and Debugging**:
   - Simulating motor control signals allows developers to validate PWM generation before connecting physical motors.
   - Waveform analysis using an oscilloscope ensures accuracy in the signal.

3. **Safety**:
   - Simulating motor control without physical motors avoids potential damage or hazards during development.

---

## **Project Goals**

- Generate a PWM signal on the STM32 GPIO pin.
- Simulate motor throttle behavior by varying the duty cycle.
- Validate the output using:
  - **Serial Console (Putty)**: Displays the current throttle percentage.
  - **Oscilloscope**: Shows the corresponding waveform.

This test provides a foundational understanding of PWM, which is essential for UAV motor control.

