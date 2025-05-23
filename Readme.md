# decrypt\_flags.py

A simple Python script that prompts for a UID, then decrypts and displays the corresponding flag using the `ft_des` algorithm, matching the original C logic.

## Overview

This repository contains **decrypt\_flags.py**, a command-line tool that implements the C program’s UID-based flag dispatch logic in Python. Users are prompted to enter a UID (decimal or hexadecimal), and if the UID matches one of the predefined values, the script will decrypt and print the corresponding flag.

## `ft_des` Algorithm Explanation

The core of this script is the `ft_des` function, a Python reimplementation of the original C algorithm:

    def ft_des(param: str) -> str:
        """
        Reimplementation of the C `ft_des` logic in Python.
        """
        arr = list(param)
        idx = 0       # position in string
        cycle = 0     # index into digits
        digits = "0123456"
    
        while idx < len(arr):
            if cycle == 6:
                cycle = 0
    
            count = ord(digits[cycle])
    
            if (idx & 1) == 0:
                # Even index: shift backwards
                for _ in range(count):
                    arr[idx] = chr(ord(arr[idx]) - 1)
                    if arr[idx] == chr(0x1F):
                        arr[idx] = '~'
            else:
                # Odd index: shift forwards
                for _ in range(count):
                    arr[idx] = chr(ord(arr[idx]) + 1)
                    if arr[idx] == chr(0x7F):
                        arr[idx] = ' '
    
            idx += 1
            cycle += 1
    
        return "".join(arr)

* **`digits` cycle**: The string `"0123456"` provides a repeating sequence of shift counts. On each character of the input, the algorithm uses the next digit’s ASCII code as the number of shifts.
* **Even indices** (`idx % 2 == 0`): Characters are shifted **backwards** (`-1` per step). If the ASCII value underflows below `0x20`, it wraps around to `~` (`0x7E`).
* **Odd indices**: Characters are shifted **forwards** (`+1` per step). If the ASCII value overflows past `0x7E`, it wraps around to space (`0x20`).
* **Cycle reset**: After processing six characters, the cycle index resets to `0` to repeat the shift counts.

This produces the decrypted flag string from an obfuscated input.

## Setup & Requirements

* Python 3.6 or later.

No additional dependencies are required.

## Usage

    $ python3 hack.py
    Enter your UID (decimal or 0xHEX): 0xBBE
    # => Prints the decrypted flag for UID 0xBBE

1. Clone or download the repository.
2. Ensure you have Python 3 installed:
    python3 --version
3. Run the script:
    python3 hack.py
4. Enter your UID when prompted. The script accepts both decimal (e.g. `3006`) and hexadecimal (e.g. `0xBBE`) formats.
