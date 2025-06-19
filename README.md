# Keylogger-Project

# 🖥️ Python Keylogger (Ethical Use)

A simple Python keylogger built with the `pynput` library for educational and ethical cybersecurity research purposes.

## About This Project

This project was created to explore how keyloggers work at a basic level, improve Python event-driven programming skills, and understand how such tools can be detected and defended against in real-world systems.

**⚠️ Disclaimer:**
> This tool is intended for educational use **on your own systems** only.  
> Please Do not use this against systems you do not own.

## 📦 Requirements

- Python 3.10+
- `pynput` library

## 📥 Installation

1. Clone this repository
2. Install required libraries: pip install pynput

## 🚀 How to run the Keylogger

- run the program in your terminal or in VScode.
- the program will start listening for keystrokes
- it is recommended to type characters in a notepad for testing
- the keystrokes will be saved in the keylog.txt
- (a sample log file is also attached for reference)

## 📜 How It Works (Explained Simply)
This keylogger uses the pynput library, which makes capturing keyboard events super clean in Python.
Without pynput, you'd have to write hundreds of lines of low-level OS-specific code in C or Assembly, directly hooking into keyboard interrupts or API calls.

Here's what happens:

When you press a key → on_press() function logs it.

When you release a key → on_release() function checks if it was the Esc key.

If Esc is pressed → it stops the program cleanly by returning False.

It also adds a timestamped header at the start of each new logging session in the log file.

Log files have extra line breaks before each new session so it’s easy to read and track multiple runs.

