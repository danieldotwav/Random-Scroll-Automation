# Random Scroll Automation

This Python program automates the process of scrolling up or down on your computer screen at random intervals. It utilizes the `pyautogui` library to control the mouse scroll, making it useful for simulating user activity or just having some fun seeing your screen scroll up and down randomly.

## Prerequisites

Before you can run this script, you must have Python installed on your computer. Additionally, you need to install the `pyautogui` library, which can be done by running the following command in your terminal:

```bash
pip install pyautogui
```

## How to Use

To get started with this random scroll automation script, follow these steps:

1. **Ensure Python and `pyautogui` are Installed**
   - Python must be installed on your computer. If you haven't installed Python yet, download and install it from the official [Python website](https://www.python.org/downloads/).
   - Install the `pyautogui` library using pip. Open your command line or terminal and run the following command:
     ```bash
     pip install pyautogui
     ```

2. **Save the Script**
   - Save the provided Python script to a file on your computer. You might name it `random_scroll.py` for convenience.

3. **Run the Script**
   - Open a terminal or command prompt window.
   - Navigate to the directory where you saved `random_scroll.py`.
   - Execute the script by typing:
     ```bash
     python random_scroll.py
     ```
   This command starts the automation script, which will begin scrolling your screen up or down at random intervals.

### Key Components of the Script

- **Scroll Amount:** The amount of scroll action in each step. Set to 1500 units by default, where negative numbers scroll down and positive numbers scroll up.
- **Pause Time:** The duration in seconds between each scroll action. It's set to 1 second by default, allowing for a brief pause between scrolls.

## How to Exit

To safely stop the script and exit the program:

- Move your mouse cursor to any of the four corners of your screen.

This action takes advantage of PyAutoGUI's fail-safe feature, which is designed to stop the script immediately if the mouse is moved to a screen corner. This is a safety mechanism to help you regain control if the script behaves unexpectedly.

## Customization

You can customize the script by editing the `scroll_amount` and `pause_time` variables. This allows you to control how much the screen scrolls and how long the script waits between each scroll. Experiment with different values to find the best experience for your needs.

## Caution

Please be aware that running this script can interfere with your normal use of the computer. It's recommended to use it in controlled environments or when you're aware of its effects on your computer's usability.