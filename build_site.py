#!/usr/bin/env python3
"""
MCES Lab Site Generator
Synchronizes experiment code files with experiments.js and generates mces-lab-offline.html.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXPERIMENTS_META = [
    {
        'id': 'exp-01',
        'number': 1,
        'title': '8051 Arithmetic, Logical & 16-Bit Operations',
        'category': '8051 Assembly',
        'desc': 'Immediate, register, direct, and indirect addressing modes, bit shifts, 16-bit addition, subtraction, multiplication, nibble swapping, register exchange, and 8-bit arithmetic in Embedded C.',
        'hardware': '8051 Microcontroller (AT89C51 / AT89S52), Keil uVision IDE, Internal RAM 30H-53H',
        'files': [
            {'name': 'Immediate_Mode_Arithmetic.asm', 'label': '1A.01 Immediate Mode (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1A_01_Immediate_Mode_Arithmetic/Immediate_Mode_Arithmetic.asm'},
            {'name': 'Register_Mode_Logical.asm', 'label': '1A.02 Register Mode (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1A_02_Register_Mode_Logical/Register_Mode_Logical.asm'},
            {'name': 'Direct_Mode_Arithmetic.asm', 'label': '1A.03 Direct Mode (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1A_03_Direct_Mode_Arithmetic/Direct_Mode_Arithmetic.asm'},
            {'name': 'Indirect_Mode_Logical.asm', 'label': '1A.04 Indirect Mode (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1A_04_Indirect_Mode_Logical/Indirect_Mode_Logical.asm'},
            {'name': 'Right_Left_Shift_With_Without_Carry.asm', 'label': '1A.05 Shift Operations (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1A_05_Right_Left_Shift_With_Without_Carry/Right_Left_Shift_With_Without_Carry.asm'},
            {'name': '16-Bit_Addition.asm', 'label': '1B.01 16-Bit Addition (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_01_16-Bit_Addition/16-Bit_Addition.asm'},
            {'name': '16-Bit_Subtraction.asm', 'label': '1B.02 16-Bit Subtraction (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_02_16-Bit_Subtraction/16-Bit_Subtraction.asm'},
            {'name': '16-Bit_Multiplication.asm', 'label': '1B.03 16-Bit Multiplication (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_03_16-Bit_Multiplication/16-Bit_Multiplication.asm'},
            {'name': 'Nibble_Swap_A9H.asm', 'label': '1B.04 Nibble Swap (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_04_Nibble_Swap_A9H/Nibble_Swap_A9H.asm'},
            {'name': 'Exchange_Register_A_B.asm', 'label': '1B.05 Exchange A & B (ASM)', 'lang': 'asm', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_05_Exchange_Register_A_B/Exchange_Register_A_B.asm'},
            {'name': '8-Bit_Arithmetic_Embedded_C.c', 'label': '1B.06 8-Bit Arithmetic (C)', 'lang': 'c', 'path': 'EXP_01_Arithmetic_Logical_and_16Bit/EXP_1B_06_8-Bit_Arithmetic_Embedded_C/8-Bit_Arithmetic_Embedded_C.c'}
        ]
    },
    {
        'id': 'exp-02',
        'number': 2,
        'title': 'Embedded C Operations on 8051',
        'category': 'Embedded C',
        'desc': 'Arithmetic and logical operations, bit manipulation, counting 1s and 0s using carry flag, roll number array streaming to Port P2, sending 0-255, -4 to +4, and fast bit toggling on P3.3.',
        'hardware': '8051 Microcontroller, Ports P0, P1, P2, P3, Keil C51 Compiler',
        'files': [
            {'name': '8-Bit_Arithmetic_in_Memory.c', 'label': '01 Arithmetic in Memory', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/01_8-Bit_Arithmetic_in_Memory/8-Bit_Arithmetic_in_Memory.c'},
            {'name': '8-Bit_Logical_Operations_to_Ports.c', 'label': '02 Logical Ops to Ports', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/02_8-Bit_Logical_Operations_to_Ports/8-Bit_Logical_Operations_to_Ports.c'},
            {'name': 'Bit_Manipulation_Shifting.c', 'label': '03 Bit Manipulation & Shift', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/03_Bit_Manipulation_Shifting/Bit_Manipulation_Shifting.c'},
            {'name': 'Count_Number_of_1s_0s.c', 'label': '04 Count 1s and 0s', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/04_Count_Number_of_1s_0s/Count_Number_of_1s_0s.c'},
            {'name': 'Roll_Number_to_Port_P2.c', 'label': '05 Roll No to Port P2', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/05_Roll_Number_to_Port_P2/Roll_Number_to_Port_P2.c'},
            {'name': 'Send_Values_0_to_255_to_Port_P1.c', 'label': '06 Send 0 to 255 to P1', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/06_Send_Values_0_to_255_to_Port_P1/Send_Values_0_to_255_to_Port_P1.c'},
            {'name': 'Send_Values_-4_to_4_to_Port_P1.c', 'label': '07 Send -4 to +4 to P1', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/07_Send_Values_-4_to_4_to_Port_P1/Send_Values_-4_to_4_to_Port_P1.c'},
            {'name': 'Bit_Toggling_P3.3_50_000_Times.c', 'label': '08 Toggle P3.3 50k Times', 'lang': 'c', 'path': 'EXP_02_Embedded_C_Operations/08_Bit_Toggling_P3.3_50_000_Times/Bit_Toggling_P3.3_50_000_Times.c'}
        ]
    },
    {
        'id': 'exp-03',
        'number': 3,
        'title': '8051 I/O Ports Programming (ASM & C)',
        'category': 'I/O Ports',
        'desc': 'Port bit toggling, software delay loop calibration, continuous square wave generation, asymmetric waves (30%/70% duty cycle, 3ms ON / 8ms OFF), port mirroring, door sensor with buzzer alarm, and bit inversion.',
        'hardware': '8051 I/O Ports P1, P2, P3, Door Sensor on P1.1, Buzzer on P1.7, CRO / Logic Analyzer',
        'files': [
            {'name': 'Toggle_Port_P1_10_Times.asm', 'label': '3A.01 Toggle P1 10x (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_01_Toggle_Port_P1_10_Times/Toggle_Port_P1_10_Times.asm'},
            {'name': 'Toggle_Port_P1_100_Times_1ms_Delay.asm', 'label': '3A.02 Toggle 100x 1ms (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_02_Toggle_Port_P1_100_Times_1ms_Delay/Toggle_Port_P1_100_Times_1ms_Delay.asm'},
            {'name': 'Toggle_P1.4_Continuously_2ms_Delay.asm', 'label': '3A.03 Toggle P1.4 2ms (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_03_Toggle_P1.4_Continuously_2ms_Delay/Toggle_P1.4_Continuously_2ms_Delay.asm'},
            {'name': 'Square_Wave_on_P1.4_10ms_Period.asm', 'label': '3A.04 Square Wave 10ms (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_04_Square_Wave_on_P1.4_10ms_Period/Square_Wave_on_P1.4_10ms_Period.asm'},
            {'name': 'Send_Port_P1_to_Port_P2_Continuously.asm', 'label': '3A.05 P1 to P2 Mirror (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_05_Send_Port_P1_to_Port_P2_Continuously/Send_Port_P1_to_Port_P2_Continuously.asm'},
            {'name': 'Asymmetric_Wave_on_P2.6_3ms_ON_8ms_OFF.asm', 'label': '3A.06 Asymmetric Wave (ASM)', 'lang': 'asm', 'path': 'EXP_03_IO_Ports/EXP_3A_06_Asymmetric_Wave_on_P2.6_3ms_ON_8ms_OFF/Asymmetric_Wave_on_P2.6_3ms_ON_8ms_OFF.asm'},
            {'name': 'Toggle_Port_P1_10_Times.c', 'label': '3B.01 Toggle P1 10x (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_01_Toggle_Port_P1_10_Times/Toggle_Port_P1_10_Times.c'},
            {'name': 'Toggle_Port_P1_100_Times_1ms_Delay.c', 'label': '3B.02 Toggle 100x 1ms (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_02_Toggle_Port_P1_100_Times_1ms_Delay/Toggle_Port_P1_100_Times_1ms_Delay.c'},
            {'name': 'Square_Wave_on_Port_P1_5ms_Delay.c', 'label': '3B.03 Square Wave P1 (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_03_Square_Wave_on_Port_P1_5ms_Delay/Square_Wave_on_Port_P1_5ms_Delay.c'},
            {'name': 'Square_Wave_on_P1.7_100ms_Period.c', 'label': '3B.04 Square Wave 100ms (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_04_Square_Wave_on_P1.7_100ms_Period/Square_Wave_on_P1.7_100ms_Period.c'},
            {'name': '30pct_70pct_Duty_Cycle_on_P2.6_100ms.c', 'label': '3B.05 30%/70% Duty Cycle (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_05_30pct_70pct_Duty_Cycle_on_P2.6_100ms/30pct_70pct_Duty_Cycle_on_P2.6_100ms.c'},
            {'name': 'Monitor_P3.6_Send_55H_to_P1_AAH_to_P2.c', 'label': '3B.06 Monitor P3.6 (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_06_Monitor_P3.6_Send_55H_to_P1_AAH_to_P2/Monitor_P3.6_Send_55H_to_P1_AAH_to_P2.c'},
            {'name': 'Door_Sensor_P1.1_Buzzer_P1.7.c', 'label': '3B.07 Door Sensor & Buzzer (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_07_Door_Sensor_P1.1_Buzzer_P1.7/Door_Sensor_P1.1_Buzzer_P1.7.c'},
            {'name': 'Invert_Bit_P1.1_Send_to_P2.7.c', 'label': '3B.08 Invert P1.1 to P2.7 (C)', 'lang': 'c', 'path': 'EXP_03_IO_Ports/EXP_3B_08_Invert_Bit_P1.1_Send_to_P2.7/Invert_Bit_P1.1_Send_to_P2.7.c'}
        ]
    },
    {
        'id': 'exp-04',
        'number': 4,
        'title': '8051 Hardware Timers (Timer 0 & Timer 1)',
        'category': 'Timers & Counters',
        'desc': 'Configuring 8051 timers in Mode 0 (13-bit), Mode 1 (16-bit), and Mode 2 (8-bit auto-reload) for accurate time delay generation: 250ms square waves, 30%/70% duty cycle, 2500Hz wave, and dual-frequency 500Hz/750Hz generator.',
        'hardware': '8051 Hardware Timers T0 & T1, Crystal Frequency 11.0592 MHz / 12 MHz, CRO',
        'files': [
            {'name': 'Toggle_P1.5_Every_250ms_Timer_0_Mode_2.asm', 'label': '01 250ms Mode 2 (ASM)', 'lang': 'asm', 'path': 'EXP_04_Timers_of_8051/01_Toggle_P1.5_Every_250ms_Timer_0_Mode_2/Toggle_P1.5_Every_250ms_Timer_0_Mode_2.asm'},
            {'name': 'Toggle_P1.5_Every_250ms_Timer_0_Mode_2.c', 'label': '01 250ms Mode 2 (C)', 'lang': 'c', 'path': 'EXP_04_Timers_of_8051/01_Toggle_P1.5_Every_250ms_Timer_0_Mode_2/Toggle_P1.5_Every_250ms_Timer_0_Mode_2.c'},
            {'name': '30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0.asm', 'label': '02 Duty Cycle Mode 0 (ASM)', 'lang': 'asm', 'path': 'EXP_04_Timers_of_8051/02_30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0/30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0.asm'},
            {'name': '30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0.c', 'label': '02 Duty Cycle Mode 0 (C)', 'lang': 'c', 'path': 'EXP_04_Timers_of_8051/02_30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0/30pct_70pct_Duty_Cycle_on_P1.4_Timer_0_Mode_0.c'},
            {'name': '2500Hz_Frequency_on_P2.7_Timer_1_Mode_1.asm', 'label': '03 2500Hz Mode 1 (ASM)', 'lang': 'asm', 'path': 'EXP_04_Timers_of_8051/03_2500Hz_Frequency_on_P2.7_Timer_1_Mode_1/2500Hz_Frequency_on_P2.7_Timer_1_Mode_1.asm'},
            {'name': '2500Hz_Frequency_on_P2.7_Timer_1_Mode_1.c', 'label': '03 2500Hz Mode 1 (C)', 'lang': 'c', 'path': 'EXP_04_Timers_of_8051/03_2500Hz_Frequency_on_P2.7_Timer_1_Mode_1/2500Hz_Frequency_on_P2.7_Timer_1_Mode_1.c'},
            {'name': 'Switch_Frequency_500Hz_750Hz_on_P1.7.c', 'label': '04 Switch 500Hz/750Hz (C)', 'lang': 'c', 'path': 'EXP_04_Timers_of_8051/04_Switch_Frequency_500Hz_750Hz_on_P1.7/Switch_Frequency_500Hz_750Hz_on_P1.7.c'}
        ]
    },
    {
        'id': 'exp-05',
        'number': 5,
        'title': '8051 Event Counters (T0 & T1)',
        'category': 'Timers & Counters',
        'desc': 'Configuring Timer 0 and Timer 1 as hardware event counters to count external clock pulses (1Hz clock input on T1 / P3.5 and T0 / P3.4) and displaying counter values on Port P1 and P2.',
        'hardware': 'Counter Pins T0 (P3.4) & T1 (P3.5), 1Hz Pulse Generator, Port P1 & P2 LEDs',
        'files': [
            {'name': 'Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2.asm', 'label': '01 Counter 1 Mode 2 (ASM)', 'lang': 'asm', 'path': 'EXP_05_Counters/01_Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2/Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2.asm'},
            {'name': 'Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2.c', 'label': '01 Counter 1 Mode 2 (C)', 'lang': 'c', 'path': 'EXP_05_Counters/01_Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2/Counter_1_Mode_2_1Hz_on_T1_P3.5_to_Port_P2.c'},
            {'name': 'Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2.asm', 'label': '02 Counter 0 Mode 1 (ASM)', 'lang': 'asm', 'path': 'EXP_05_Counters/02_Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2/Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2.asm'},
            {'name': 'Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2.c', 'label': '02 Counter 0 Mode 1 (C)', 'lang': 'c', 'path': 'EXP_05_Counters/02_Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2/Counter_0_Mode_1_1Hz_on_T0_P3.4_to_P1_P2.c'}
        ]
    },
    {
        'id': 'exp-06',
        'number': 6,
        'title': 'Serial Communication (UART) at Multiple Baud Rates',
        'category': 'Serial Communication',
        'desc': 'Configuring 8051 UART with Timer 1 in Mode 2 baud rate generator: transmitting character \'E\' at 9600 baud, continuous \'EVL\' at 4800 baud, student roll number at 2400 baud, and elevator OVERLOAD alert.',
        'hardware': 'UART TxD (P3.1), RxD (P3.0), MAX232 Level Converter, Serial Terminal (9600/4800/2400 8-N-1)',
        'files': [
            {'name': 'Transfer_E_Serially_at_9600_Baud.asm', 'label': '01 Transfer E 9600 (ASM)', 'lang': 'asm', 'path': 'EXP_06_Serial_Communication/01_Transfer_E_Serially_at_9600_Baud/Transfer_E_Serially_at_9600_Baud.asm'},
            {'name': 'Transfer_E_Serially_at_9600_Baud.c', 'label': '01 Transfer E 9600 (C)', 'lang': 'c', 'path': 'EXP_06_Serial_Communication/01_Transfer_E_Serially_at_9600_Baud/Transfer_E_Serially_at_9600_Baud.c'},
            {'name': 'Transfer_EVL_Continuously_at_4800_Baud.asm', 'label': '02 Transfer EVL 4800 (ASM)', 'lang': 'asm', 'path': 'EXP_06_Serial_Communication/02_Transfer_EVL_Continuously_at_4800_Baud/Transfer_EVL_Continuously_at_4800_Baud.asm'},
            {'name': 'Transfer_EVL_Continuously_at_4800_Baud.c', 'label': '02 Transfer EVL 4800 (C)', 'lang': 'c', 'path': 'EXP_06_Serial_Communication/02_Transfer_EVL_Continuously_at_4800_Baud/Transfer_EVL_Continuously_at_4800_Baud.c'},
            {'name': 'Transfer_Roll_Number_at_2400_Baud.asm', 'label': '03 Transfer Roll No 2400 (ASM)', 'lang': 'asm', 'path': 'EXP_06_Serial_Communication/03_Transfer_Roll_Number_at_2400_Baud/Transfer_Roll_Number_at_2400_Baud.asm'},
            {'name': 'Transfer_Roll_Number_at_2400_Baud.c', 'label': '03 Transfer Roll No 2400 (C)', 'lang': 'c', 'path': 'EXP_06_Serial_Communication/03_Transfer_Roll_Number_at_2400_Baud/Transfer_Roll_Number_at_2400_Baud.c'},
            {'name': 'Elevator_OVERLOAD_at_Count_5_9600_Baud.asm', 'label': '04 Elevator Overload (ASM)', 'lang': 'asm', 'path': 'EXP_06_Serial_Communication/04_Elevator_OVERLOAD_at_Count_5_9600_Baud/Elevator_OVERLOAD_at_Count_5_9600_Baud.asm'},
            {'name': 'Elevator_OVERLOAD_at_Count_5_9600_Baud.c', 'label': '04 Elevator Overload (C)', 'lang': 'c', 'path': 'EXP_06_Serial_Communication/04_Elevator_OVERLOAD_at_Count_5_9600_Baud/Elevator_OVERLOAD_at_Count_5_9600_Baud.c'}
        ]
    },
    {
        'id': 'exp-07',
        'number': 7,
        'title': 'UART LED Remote Control',
        'category': 'Serial Communication',
        'desc': 'Receiving commands over 8051 serial port at 9600 baud: turning LED ON on P1.2 upon receiving character \'1\', and turning LED OFF upon receiving \'0\'.',
        'hardware': 'UART RxD (P3.0), LED on P1.2, Serial Terminal / Bluetooth Module at 9600 Baud',
        'files': [
            {'name': 'UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2.asm', 'label': '01 UART LED Control (ASM)', 'lang': 'asm', 'path': 'EXP_07_UART_LED_Control/01_UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2/UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2.asm'},
            {'name': 'UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2.c', 'label': '01 UART LED Control (C)', 'lang': 'c', 'path': 'EXP_07_UART_LED_Control/01_UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2/UART_Receive_1_LED_ON_0_LED_OFF_on_P1.2.c'}
        ]
    },
    {
        'id': 'exp-08',
        'number': 8,
        'title': '8051 Hardware & Timer Interrupts',
        'category': 'Interrupts',
        'desc': 'Interrupt Service Routines (ISRs) for Timer 0, Timer 1, Serial UART, and External Hardware Interrupts (INT0 & INT1); concurrent wave generation, port mirroring in background, and fire alarm siren.',
        'hardware': 'INT0 (P3.2), INT1 (P3.3), P1.2, P2.4, P3.6, Buzzer, UART TxD/RxD, CRO',
        'files': [
            {'name': '1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts.asm', 'label': '01 1kHz & 4kHz Mode 1 (ASM)', 'lang': 'asm', 'path': 'EXP_08_Interrupts/01_1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts/1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts.asm'},
            {'name': '1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts.c', 'label': '01 1kHz & 4kHz Mode 1 (C)', 'lang': 'c', 'path': 'EXP_08_Interrupts/01_1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts/1kHz_P1.2_4kHz_P2.4_Waves_Mode_1_Interrupts.c'},
            {'name': 'P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2.asm', 'label': '02 3kHz & 6kHz Mode 2 (ASM)', 'lang': 'asm', 'path': 'EXP_08_Interrupts/02_P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2/P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2.asm'},
            {'name': 'P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2.c', 'label': '02 3kHz & 6kHz Mode 2 (C)', 'lang': 'c', 'path': 'EXP_08_Interrupts/02_P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2/P1toP2_3kHz_P0.6_6kHz_P3.6_Waves_Mode_2.c'},
            {'name': 'Serial_RxtoP0_P1toSerial_P2_5kHz_Wave_on_P3.6.asm', 'label': '03 Serial & 5kHz Wave (ASM)', 'lang': 'asm', 'path': 'EXP_08_Interrupts/03_Serial_RxtoP0_P1toSerial_P2_5kHz_Wave_on_P3.6/Serial_RxtoP0_P1toSerial_P2_5kHz_Wave_on_P3.6.asm'},
            {'name': 'External_Interrupts_INT0_3_INT1_-5.c', 'label': '04 INT0 & INT1 Counter (C)', 'lang': 'c', 'path': 'EXP_08_Interrupts/04_External_Interrupts_INT0_3_INT1_-5/External_Interrupts_INT0_3_INT1_-5.c'},
            {'name': 'INT0_Fire_Alarm_Square_Wave_on_P2.4_Send_FIRE.c', 'label': '05 Fire Alarm on INT0 (C)', 'lang': 'c', 'path': 'EXP_08_Interrupts/05_INT0_Fire_Alarm_Square_Wave_on_P2.4_Send_FIRE/INT0_Fire_Alarm_Square_Wave_on_P2.4_Send_FIRE.c'}
        ]
    },
    {
        'id': 'exp-09',
        'number': 9,
        'title': 'LED, Buzzer & 7-Segment Display Interfacing',
        'category': 'Peripheral Interfacing',
        'desc': 'Interfacing digital output devices: LED flashing on P1.4 with 500ms delay, Piezo buzzer tone generation on P1.5, and multi-digit multiplexed common-cathode 7-segment display on P1 (digit select) and P2 (segment data).',
        'hardware': 'LED on P1.4, Buzzer on P1.5, Multiplexed 7-Segment Display on Port P1 & P2',
        'files': [
            {'name': 'LED_Blinking_P1.4.c', 'label': '01 LED Blinking P1.4 (C)', 'lang': 'c', 'path': 'EXP_09_LED_Buzzer_7Segment/01_LED_Blinking_P1.4/LED_Blinking_P1.4.c'},
            {'name': 'Buzzer_Interfacing_P1.5.c', 'label': '02 Buzzer Interfacing P1.5 (C)', 'lang': 'c', 'path': 'EXP_09_LED_Buzzer_7Segment/02_Buzzer_Interfacing_P1.5/Buzzer_Interfacing_P1.5.c'},
            {'name': '7-Segment_Display_Port_P1_P2.c', 'label': '03 7-Segment Display (C)', 'lang': 'c', 'path': 'EXP_09_LED_Buzzer_7Segment/03_7-Segment_Display_Port_P1_P2/7-Segment_Display_Port_P1_P2.c'}
        ]
    },
    {
        'id': 'exp-10',
        'number': 10,
        'title': 'DC Motor Interfacing with 8051',
        'category': 'Peripheral Interfacing',
        'desc': 'Controlling DC Motor direction (clockwise and counter-clockwise) using L293D / driver circuit connected to 8051 microcontroller pins P1.6 and P1.7.',
        'hardware': '8051 MCU, L293D / Driver IC, 12V/5V DC Motor, Control Pins P1.6 & P1.7',
        'files': [
            {'name': 'DC_Motor_Rotation_P1.6_P1.7.c', 'label': '01 DC Motor Rotation (C)', 'lang': 'c', 'path': 'EXP_10_DC_Motor/01_DC_Motor_Rotation_P1.6_P1.7/DC_Motor_Rotation_P1.6_P1.7.c'}
        ]
    },
    {
        'id': 'exp-11',
        'number': 11,
        'title': 'Stepper Motor Interfacing with 8051',
        'category': 'Peripheral Interfacing',
        'desc': 'Controlling 4-phase unipolar stepper motor using stepping sequence 0xF1, 0xF2, 0xF4, 0xF8 on Port P1 with calibrated inter-step delay for smooth angular displacement.',
        'hardware': '8051 MCU, ULN2003 Driver Darlington Array, 4-Phase Stepper Motor on Port P1',
        'files': [
            {'name': 'Stepper_Motor_Rotation_0xF1_to_0xF2_to_0xF4_to_0xF8.c', 'label': '01 Stepper Motor Sequence (C)', 'lang': 'c', 'path': 'EXP_11_Stepper_Motor/01_Stepper_Motor_Rotation_0xF1_to_0xF2_to_0xF4_to_0xF8/Stepper_Motor_Rotation_0xF1_to_0xF2_to_0xF4_to_0xF8.c'}
        ]
    },
    {
        'id': 'exp-12',
        'number': 12,
        'title': '16x2 LCD Interfacing with 8051 (4-Bit Mode)',
        'category': 'Peripheral Interfacing',
        'desc': 'Interfacing 16x2 alphanumeric LCD display to 8051 microcontroller in 4-bit nibble mode using Port P2 (RS=P2.7, RW=P2.5, EN=P2.6) to display student Name and Roll Number.',
        'hardware': '16x2 Alphanumeric LCD (HD44780 compatible), Port P2, RS (P2.7), RW (P2.5), EN (P2.6)',
        'files': [
            {'name': '16x2_LCD_4-Bit_Display_Name_Roll_No._on_Port_P2.c', 'label': '01 16x2 LCD 4-Bit Mode (C)', 'lang': 'c', 'path': 'EXP_12_16x2_LCD_Interfacing/01_16x2_LCD_4-Bit_Display_Name_Roll_No._on_Port_P2/16x2_LCD_4-Bit_Display_Name_Roll_No._on_Port_P2.c'}
        ]
    },
    {
        'id': 'exp-13',
        'number': 13,
        'title': '4x4 Matrix Keypad & 16x2 LCD Interfacing',
        'category': 'Peripheral Interfacing',
        'desc': 'Matrix keypad scanning algorithm: row drive on P2.0-P2.3, column reading on P2.4-P2.7, contact bounce filter, key code detection (0-F), and immediate display on 16x2 LCD.',
        'hardware': '4x4 Matrix Keypad on Port P2, 16x2 Alphanumeric LCD on Port P1',
        'files': [
            {'name': '4x4_Matrix_Keypad_Scan_0_F_to_16x2_LCD_EVL_KEYPAD.c', 'label': '01 Keypad Scan to LCD (C)', 'lang': 'c', 'path': 'EXP_13_Keypad_and_LCD/01_4x4_Matrix_Keypad_Scan_0_F_to_16x2_LCD_EVL_KEYPAD/4x4_Matrix_Keypad_Scan_0_F_to_16x2_LCD_EVL_KEYPAD.c'}
        ]
    },
    {
        'id': 'exp-14',
        'number': 14,
        'title': 'Waveform Generation using 8051 & DAC0808',
        'category': 'Analog & DAC',
        'desc': 'Interfacing 8-bit Digital-to-Analog Converter (DAC0808) with 8051 microcontroller on Port P1: generating Square wave, Ascending Sawtooth, Descending Sawtooth, Triangular wave, and Sine wave.',
        'hardware': '8051 MCU, DAC0808 / DAC0800 8-Bit DAC IC, LM741 Op-Amp I-V Converter, Port P1, CRO',
        'files': [
            {'name': 'Square_Wave.c', 'label': '01 Square Wave (C)', 'lang': 'c', 'path': 'EXP_14_Waveform_Generation_DAC0808/01_Square_Wave/Square_Wave.c'},
            {'name': 'Sawtooth_Ascending.c', 'label': '02 Sawtooth Ascending (C)', 'lang': 'c', 'path': 'EXP_14_Waveform_Generation_DAC0808/02_Sawtooth_Ascending/Sawtooth_Ascending.c'},
            {'name': 'Sawtooth_Descending.c', 'label': '03 Sawtooth Descending (C)', 'lang': 'c', 'path': 'EXP_14_Waveform_Generation_DAC0808/03_Sawtooth_Descending/Sawtooth_Descending.c'},
            {'name': 'Triangular_Wave.c', 'label': '04 Triangular Wave (C)', 'lang': 'c', 'path': 'EXP_14_Waveform_Generation_DAC0808/04_Triangular_Wave/Triangular_Wave.c'},
            {'name': 'Sinusoidal_Wave.c', 'label': '05 Sinusoidal Wave (C)', 'lang': 'c', 'path': 'EXP_14_Waveform_Generation_DAC0808/05_Sinusoidal_Wave/Sinusoidal_Wave.c'}
        ]
    },
    {
        'id': 'exp-15',
        'number': 15,
        'title': 'LED & Buzzer Interfacing on Arduino Development Board',
        'category': 'Arduino Development Board',
        'desc': 'Configuring GPIO pins on Arduino Uno: flashing on-board / external LED on digital pin 13 with 1000ms delay, and driving an audible piezo buzzer on digital pin 8.',
        'hardware': 'Arduino Uno (ATmega328P), Built-in / External LED (Pin 13), Piezo Buzzer (Pin 8), Arduino IDE',
        'files': [
            {'name': 'LED_Blinking.ino', 'label': '01 LED Blinking (Ino)', 'lang': 'cpp', 'path': 'EXP_15_Arduino_LED_and_Buzzer/01_LED_Blinking/LED_Blinking.ino'},
            {'name': 'Buzzer_Interfacing.ino', 'label': '02 Buzzer Interfacing (Ino)', 'lang': 'cpp', 'path': 'EXP_15_Arduino_LED_and_Buzzer/02_Buzzer_Interfacing/Buzzer_Interfacing.ino'}
        ]
    },
    {
        'id': 'exp-16',
        'number': 16,
        'title': '16x2 LCD Display on Arduino Development Board',
        'category': 'Arduino Development Board',
        'desc': 'Interfacing 16x2 LCD with Arduino Uno using LiquidCrystal library (RS=12, EN=11, D4=5, D5=4, D6=3, D7=2), printing student Name on Line 1, Roll Number on Line 2, and display blinking.',
        'hardware': 'Arduino Uno, 16x2 LCD Display, 10k Potentiometer (Contrast), Pins 12, 11, 5, 4, 3, 2',
        'files': [
            {'name': '16x2_LCD_Display_Name_Roll_No.ino', 'label': '01 16x2 LCD Display (Ino)', 'lang': 'cpp', 'path': 'EXP_16_Arduino_16x2_LCD/01_16x2_LCD_Display_Name_Roll_No/16x2_LCD_Display_Name_Roll_No.ino'}
        ]
    },
    {
        'id': 'exp-17',
        'number': 17,
        'title': 'Ultrasonic Distance Measurement (Arduino)',
        'category': 'Arduino Development Board',
        'desc': 'Interfacing HC-SR04 Ultrasonic Distance Sensor with Arduino Uno: generating 10us trigger pulse on pin 6, reading echo pulse duration using pulseIn(7, HIGH), computing distance in cm, and logging to Serial Monitor.',
        'hardware': 'Arduino Uno, HC-SR04 Ultrasonic Sensor (Trig: Pin 6, Echo: Pin 7), Serial Monitor at 9600 Baud',
        'files': [
            {'name': 'Ultrasonic_Distance_Measurement.ino', 'label': '01 Ultrasonic Distance (Ino)', 'lang': 'cpp', 'path': 'EXP_17_Arduino_Ultrasonic_Sensor/01_Ultrasonic_Distance_Measurement/Ultrasonic_Distance_Measurement.ino'}
        ]
    }
]

def build():
    print('Starting build...')
    # Load code
    for exp in EXPERIMENTS_META:
        for f in exp['files']:
            p = os.path.join(BASE_DIR, f['path'])
            if os.path.exists(p):
                with open(p, 'r', errors='ignore') as fp:
                    f['code'] = fp.read()
            else:
                print(f'Warning: file not found: {p}')
                f['code'] = ''

    # Write experiments.js
    exp_js_path = os.path.join(BASE_DIR, 'experiments.js')
    with open(exp_js_path, 'w') as fp:
        fp.write('const EXPERIMENTS = ' + json.dumps(EXPERIMENTS_META, indent=2) + ';\n')
    print('Updated experiments.js')

    # Read components for offline bundle
    with open(os.path.join(BASE_DIR, 'index.html')) as f:
        html = f.read()
    with open(os.path.join(BASE_DIR, 'styles.css')) as f:
        css = f.read()
    with open(exp_js_path) as f:
        exp_js = f.read()
    with open(os.path.join(BASE_DIR, 'app.js')) as f:
        app_js = f.read()

    # Create standalone offline bundle
    html_bundle = html.replace('<link rel=\"stylesheet\" href=\"styles.css\">', f'<style>\n{css}\n</style>')
    scripts = f'<script>\n{exp_js}\n</script>\n<script>\n{app_js}\n</script>'
    html_bundle = html_bundle.replace('<script src=\"experiments.js\"></script>\n  <script src=\"app.js\"></script>', scripts)

    offline_path = os.path.join(BASE_DIR, 'mces-lab-offline.html')
    with open(offline_path, 'w') as f:
        f.write(html_bundle)
    print(f'Updated mces-lab-offline.html ({len(html_bundle)} bytes)')
    print('Build finished successfully!')

if __name__ == '__main__':
    build()
