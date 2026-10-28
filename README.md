# MCES Lab - 8051 Microcontroller & Embedded Systems

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Live-Web_Viewer-brightgreen.svg)](https://hareeshwar-04.github.io/mces-lab/)
[![Experiments](https://img.shields.io/badge/Experiments-17_Labs-orange.svg)](#experiments-index)
[![Target](https://img.shields.io/badge/Target-8051_%7C_Arduino_Uno-blueviolet.svg)](#hardware--tools)

A comprehensive, fully verified, interactive laboratory code repository and web viewer for **Microcontrollers & Embedded Systems (MCES)**. Aligned with the official academic syllabus and laboratory observation manuals of **CVR College of Engineering**.

---

## 🌟 Interactive Web Viewer

The repository includes a modern, high-contrast, zero-dependency web viewer:
- ⚡ **Live Search**: Instant multi-keyword search across titles, descriptions, port pins, and code text.
- 🗂️ **Category Filtering**: Filter by 8051 Assembly, Embedded C, I/O Ports, Timers, Serial UART, Interrupts, Peripherals, and Arduino.
- 📋 **One-Click Copy & Download**: Directly copy code snippets or download individual source files (`.asm`, `.c`, `.ino`).
- 🌐 **Offline Bundle**: Double-click `mces-lab-offline.html` to run the complete site offline without needing an active internet connection.

---

## 📚 Experiments Index

| Exp # | Experiment Title | Category | Programs / Variants | Target Platform & Port Pins |
| :---: | :--- | :---: | :---: | :--- |
| **01** | [Arithmetic, Logical & 16-Bit Operations](EXP_01_Arithmetic_Logical_and_16Bit/) | 8051 Assembly & C | 11 Programs | Internal RAM (30H–53H), Registers A, B, R0–R7 |
| **02** | [Embedded C Operations on 8051](EXP_02_Embedded_C_Operations/) | Embedded C | 8 Programs | Keil C51, Ports P0, P1, P2, P3 |
| **03** | [I/O Ports Programming](EXP_03_IO_Ports/) | I/O Ports | 14 Programs (ASM & C) | Ports P1, P2, P3, Door Sensor (P1.1), Buzzer (P1.7) |
| **04** | [Hardware Timers (Timer 0 & Timer 1)](EXP_04_Timers_of_8051/) | Timers & Counters | 7 Programs (ASM & C) | Modes 0, 1, 2, Crystal 11.0592 MHz / 12 MHz, P1.4, P1.5, P2.7 |
| **05** | [Hardware Event Counters](EXP_05_Counters/) | Timers & Counters | 4 Programs (ASM & C) | T1 (P3.5), T0 (P3.4), External 1Hz Pulse Generator |
| **06** | [Serial Communication (UART)](EXP_06_Serial_Communication/) | Serial UART | 8 Programs (ASM & C) | UART TxD (P3.1), RxD (P3.0), 9600, 4800, 2400 Baud |
| **07** | [UART Remote LED Control](EXP_07_UART_LED_Control/) | Serial UART | 2 Programs (ASM & C) | UART RxD (P3.0), LED on P1.2 (ASCII '1' = ON, '0' = OFF) |
| **08** | [Hardware & Timer Interrupts](EXP_08_Interrupts/) | Interrupts | 7 Programs (ASM & C) | INT0 (P3.2), INT1 (P3.3), Timer 0, Timer 1, UART ISR |
| **09** | [LED, Buzzer & 7-Segment Interfacing](EXP_09_LED_Buzzer_7Segment/) | Peripheral Interfacing | 3 Programs (C) | LED on P1.4, Buzzer on P1.5, 7-Segment Multiplexed (P1/P2) |
| **10** | [DC Motor Interfacing with 8051](EXP_10_DC_Motor/) | Peripheral Interfacing | 1 Program (C) | L293D Driver, Direction Pins P1.6 & P1.7 |
| **11** | [Stepper Motor Interfacing with 8051](EXP_11_Stepper_Motor/) | Peripheral Interfacing | 1 Program (C) | ULN2003 Driver, Port P1 (0xF1, 0xF2, 0xF4, 0xF8) |
| **12** | [16x2 LCD Interfacing (4-Bit Mode)](EXP_12_16x2_LCD_Interfacing/) | Peripheral Interfacing | 1 Program (C) | HD44780 16x2 LCD, Port P2, RS (P2.7), RW (P2.5), EN (P2.6) |
| **13** | [4x4 Matrix Keypad & 16x2 LCD](EXP_13_Keypad_and_LCD/) | Peripheral Interfacing | 1 Program (C) | 4x4 Keypad on P2, 16x2 LCD on P1, Debounce & Scan |
| **14** | [Waveform Generation using DAC0808](EXP_14_Waveform_Generation_DAC0808/) | Analog & DAC | 5 Waveforms (C) | DAC0808 on P1: Square, Sawtooth (Asc/Desc), Triangular, Sine |
| **15** | [Arduino LED & Buzzer Interfacing](EXP_15_Arduino_LED_and_Buzzer/) | Arduino Board | 2 Sketches (.ino) | Arduino Uno, LED_BUILTIN (Pin 13), Piezo Buzzer (Pin 8) |
| **16** | [Arduino 16x2 LCD Display](EXP_16_Arduino_16x2_LCD/) | Arduino Board | 1 Sketch (.ino) | LiquidCrystal (RS=12, EN=11, D4=5, D5=4, D6=3, D7=2) |
| **17** | [Arduino Ultrasonic Distance Sensor](EXP_17_Arduino_Ultrasonic_Sensor/) | Arduino Board | 1 Sketch (.ino) | HC-SR04, Trig (Pin 6), Echo (Pin 7), Serial Output |

---

## 🛠️ Code Fixes & Structural Integrity

All source codes maintain the exact syntactic and stylistic structure of the original observation notes while resolving critical runtime issues:
1. **Embedded Infinite Loop Safing**: Added `while (1);` termination loops across pure computation Embedded C routines (`EXP_1B_06`, `EXP_02_01`, `EXP_02_02`, `EXP_02_03`, `EXP_02_06`, `EXP_02_07`, `EXP_02_08`) to prevent CPU reset and runaway instruction execution.
2. **Buffer Overrun Protection on 16x2 LCD (`EXP_12`)**: Corrected string display loop bounds for `"Name"` from `c < 6` to `c < 4` to prevent displaying stack garbage bytes on the LCD screen, and separated the 4-bit initialization from the static display loop.
3. **Carry Flag Shifting (`EXP_02_04`)**: Fixed Keil C51 bit-shift carry capture (`carry = a & 0x01; a >>= 1;`) ensuring hardware carry count evaluates correctly.
4. **Nested Assembly Delay Loop Fix (`EXP_3A_03`)**: Corrected label ordering in 3-tier delay routine (`ABC`, `MNO`, `XYZ`) ensuring register counters reload and count down properly.
5. **Mode 2 Counter Re-arming (`EXP_05_01`)**: Updated loop return target in ASM from `SJMP EVL` to `SJMP MC` to re-arm `TR1` upon timer overflow, and wrapped the C version in `while(1)`.
6. **UART Roll Number Null-Byte Safety (`EXP_06_03`)**: Restricted ASCII character transmission loop from `i < 11` to `i < 10` so the string terminates without transmitting an unwanted null byte (`\0`).
7. **Arduino Buzzer & Ultrasonic (`EXP_15`, `EXP_17`)**: Defined digital output pin (`const int BUZZER_PIN = 8;`) instead of undefined constant `BUZZ_BUILTIN`, and added missing `Serial.println(distance);` print call in HC-SR04 ultrasonic echo handler.

---

## 🚀 Getting Started

### 1. Keil &micro;Vision C51 / A51
1. Open Keil &micro;Vision and click **Project &rarr; New &micro;Vision Project...**.
2. Select target device **Microchip / Atmel &rarr; AT89C51** (or AT89S52).
3. Copy standard startup code `STARTUP.A51` when prompted.
4. Add desired `.asm` or `.c` files to Source Group 1.
5. In **Project &rarr; Options for Target &rarr; Output**, enable **Create HEX File**.
6. Click **Rebuild** (`F7`) and start the Debug Session (`Ctrl + F5`).
7. Open **View &rarr; Periodic Window &rarr; I/O Ports** or **Serial Window #1** to observe output.

### 2. Arduino IDE
1. Open the `.ino` sketch in Arduino IDE.
2. Select **Tools &rarr; Board &rarr; Arduino Uno**.
3. Choose the appropriate Serial Port (**Tools &rarr; Port**).
4. Click **Verify** (`Ctrl + R`) and **Upload** (`Ctrl + U`).
5. Open **Serial Monitor** (`Ctrl + Shift + M`) set to **9600 baud**.

---

## 💻 Running the Web Viewer Locally

You can run the web viewer directly without installing any web server:
```bash
# Simply open in your default browser
xdg-open index.html
# Or open the self-contained offline bundle
xdg-open mces-lab-offline.html
```

Or serve via Python's built-in HTTP server:
```bash
python3 -m http.server 8080
```
Open [http://localhost:8080](http://localhost:8080) in any web browser.

---

## 📄 License
This project is licensed under the MIT License.
