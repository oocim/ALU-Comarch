# 🧠 4-Bit Arithmetic Logic Unit (ALU) – Python Implementation

## 📘 Overview

This project is a software simulation of a **4-bit Arithmetic Logic Unit (ALU)** using Python. It models the core logic unit found in digital processors, capable of performing arithmetic and bitwise logical operations on two 4-bit binary numbers.

---

## ⚙️ Features

- Accepts two 4-bit binary inputs (A and B)
- Performs the following operations:
  - ➕ Addition
  - ➖ Subtraction
  - 🔁 Bitwise AND (`&`)
  - 🔁 Bitwise OR (`|`)
  - 🔁 Bitwise XOR (`^`)
  - ❗ Bitwise NOT (`~`) on A
- Displays result and detects overflow

---

## 🧩 Functional Modules

- Contains modular functions for:
  - `add(a, b)`
  - `subtract(a, b)`
  - `bitwise_and(a, b)`
  - `bitwise_or(a, b)`
  - `bitwise_xor(a, b)`
  - `bitwise_not(a)`
- Handles overflow and 4-bit constraints
- Handles input/output operations
- Accepts binary strings for A and B
- Allows user to select operation
- Calls the corresponding function from `ALU` class

---

## 🚀 How to Run

### Prerequisites

- Python 3.6 or later

### Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/oocim/ALU-Comarch
   cd 4bit-alu
   ```

2. Run the ALU using:
   ```bash
   python main.py
   ```

---

## 🧪 Sample Input & Output

```bash
Enter 4-bit input A: 0101
Enter 4-bit input B: 0011
Choose operation (+, -, &, |, ^, ~): +
Result: 1000
Overflow: No
```

---

## 💻 System Requirements

| Requirement     | Specification                |
|-----------------|------------------------------|
| OS              | Windows / Linux / macOS      |
| Python Version  | 3.6 or later                 |
| IDE (optional)  | VSCode, PyCharm              |
| External Libs   | None (uses standard Python)  |
