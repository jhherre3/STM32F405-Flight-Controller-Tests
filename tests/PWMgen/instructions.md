# Instructions: Testing PWM Motor Simulation on STM32

## **Overview**

This guide explains how to test a PWM motor simulation on an STM32 microcontroller. The PWM signal is visualized using both Putty (serial console) and an oscilloscope. The duty cycle varies to simulate throttle changes for motor control.

---

## **Hardware Requirements**

1. **STM32F405 Feather Board**.
2. **Oscilloscope** or **Logic Analyzer** for waveform visualization.
3. **USB Cable** to connect STM32 to your computer.

---

## **Software Requirements**

1. **CircuitPython** installed on the STM32.
2. **Putty** or a similar serial console application.

---

## **Setup Instructions**

### **1. Wiring**

| **STM32 Pin** | **Connection**             |
|---------------|----------------------------|
| `D9`          | Connect to Oscilloscope/Logic Analyzer (Signal). |
| `GND`         | Connect to Oscilloscope Ground.                 |

---

### **2. Upload Code**

1. Save the provided Python code to a file named `code.py`.
2. Copy `code.py` to the root directory of the STM32 microcontroller.

---

### **3. Serial Console Setup**

1. Open **Putty** or your preferred serial console.
2. Configure Putty for the STM32 serial port:
   - **Baud Rate**: `9600`
   - **Data Bits**: `8`
   - **Stop Bits**: `1`
   - **Parity**: None
   - **Flow Control**: None

3. Connect to the STM32 and observe the throttle percentage updates.

---

### **4. Testing with Oscilloscope**

1. Attach the oscilloscope probe to the `D9` pin and the ground lead to `GND`.
2. Observe the PWM waveform on the oscilloscope:
   - **Small Waveform**: Corresponds to lower throttle (smaller duty cycle).
   - **Larger Waveform**: Corresponds to higher throttle (larger duty cycle).

---

## **How the Code Works**

1. **PWM Initialization**:
   - The PWM signal is generated on `D9` with a frequency of **50 Hz**, typical for motor ESCs.

2. **Throttle Simulation**:
   - The duty cycle increases from **0% to 100%** and then decreases back to **0%**, simulating motor throttle behavior.

3. **Serial Output**:
   - The current throttle percentage is printed to the serial console for monitoring.

4. **Waveform Visualization**:
   - The duty cycle directly affects the waveform's high time (pulse width), observable on the oscilloscope.

---

## **Expected Results**

1. **Serial Console**:
   - The console will display throttle percentages:
     ```plaintext
     Throttle: 0.0%
     Throttle: 25.0%
     Throttle: 50.0%
     Throttle: 100.0%
     ```

2. **Oscilloscope**:
   - The PWM waveform will vary:
     - **Small pulse width** for low throttle.
     - **Larger pulse width** for high throttle.

---

## **Troubleshooting**

1. **No Output on Serial Console**:
   - Ensure Putty is connected to the correct COM port.
   - Verify the baud rate is set to `9600`.

2. **No Waveform on Oscilloscope**:
   - Check the connections (D9 → Signal, GND → Ground).
   - Verify the PWM frequency is set to `50 Hz`.

---

## **Conclusion**

This project demonstrates the generation of PWM signals on an STM32, simulating motor control for UAV applications. By analyzing the output in Putty and on an oscilloscope, you can validate the accuracy of the PWM signal.
