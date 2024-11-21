# Instructions: ESP32 and STM32 Communication Test

This document provides step-by-step instructions to perform a communication test between an STM32 and an ESP32. The goal of this test is to demonstrate how an STM32 can send messages to an ESP32 via UART, with the ESP32 hosting a webpage to display the messages. The test was designed to gradually build up functionality, from simple message verification to hosting a live webpage.

---

## **Step 1: Flash Basic Test Code to STM32**
1. Open the Arduino IDE or another suitable programming environment for STM32.
2. Flash the STM32 with a basic test program that sends messages (e.g., `"Hello from STM32"`) via UART.
3. Verify the message is being sent:
   - Open Putty or a Serial Monitor.
   - Connect to the STM32's COM port at `9600 baud`.
   - Confirm that `"Hello from STM32"` (or a similar message) appears every second.

---

## **Step 2: Flash Basic Test Code to ESP32**
1. Write a simple ESP32 program that:
   - Connects to your home Wi-Fi or creates an access point.
   - Displays its IP address on the Serial Monitor.
2. Upload this code to the ESP32 using the Arduino IDE or PlatformIO.
3. Verify that the ESP32 connects to Wi-Fi or successfully creates an access point:
   - Open the Serial Monitor.
   - Confirm the displayed IP address or access point details.

---

## **Step 3: Connect STM32 to ESP32**
1. Connect the STM32 to the ESP32 via UART using the following pin connections:
   | STM32 Pin | ESP32 Pin  | Description                     |
   |-----------|------------|---------------------------------|
   | TX        | RX (GPIO16)| STM32 TX to ESP32 RX            |
   | GND       | GND        | Common ground between devices.  |
   | 3.3V      | 3.3V       | Power for the STM32 if required. |

2. Ensure the STM32 is powered on and continues to send its test message via UART.

---

## **Step 4: Add Message Handling to ESP32**
1. Update the ESP32 firmware to include:
   - UART functionality to receive messages from the STM32.
   - Hosting a basic webpage that displays the received messages.
2. Flash the updated firmware to the ESP32.
3. Verify functionality:
   - Open the Serial Monitor.
   - Confirm that the ESP32 receives and displays the message from the STM32.

---

## **Step 5: Access the Webpage**
1. Connect to the ESP32's Wi-Fi network (or ensure the ESP32 is on the same network as your device).
2. Open a browser and navigate to the IP address displayed in the ESP32's Serial Monitor.
3. Verify that the webpage displays the message received from the STM32.

---

## **Testing Notes**
- **Initial Verification**: Start by confirming STM32 messages can be read via Putty or the Serial Monitor.
- **Wi-Fi Functionality**: Verify that the ESP32 successfully connects to the network or creates an access point.
- **Webpage Display**: Ensure the live message updates are visible on the ESP32-hosted webpage.

---

## **Troubleshooting**
1. **No Wi-Fi Connection**:
   - Double-check the SSID and password in the ESP32 firmware.
   - Ensure your device is on the same Wi-Fi network as the ESP32.

2. **No STM32 Messages**:
   - Confirm the STM32 is powered and running the test code.
   - Verify the UART wiring between the STM32 and ESP32 (TX to RX and GND).

3. **No Webpage**:
   - Ensure the ESP32 is hosting a server. Recheck the Serial Monitor for the IP address.
   - Try refreshing the browser or using a different device.

---

## **Summary**
This test progresses through the following stages:
1. Flash basic UART test code to the STM32.
2. Flash ESP32 firmware to verify Wi-Fi and webpage hosting.
3. Establish UART communication between the STM32 and ESP32.
4. Display live STM32 messages on a webpage hosted by the ESP32.

By following these steps, you validate both the STM32's ability to send data and the ESP32's capability to receive and display it, demonstrating the potential for integrating UART communication into a more complex system with wireless capabilities.

