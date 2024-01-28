# Snake Game Automation

Automate playing the Google Snake Game using Selenium and Python. This script navigates to the Google Snake Game, configures game settings, and controls the snake using keyboard inputs to achieve the highest score.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Selenium WebDriver
- PyAutoGUI
- Pynput
- ChromeDriver (compatible with your Chrome version)

### Installing

A step by step series of examples that tell you how to get the automation environment running.

1. **Install Python Packages**

   Open a terminal or command prompt and install the required Python packages using pip:

```bash
   pip install selenium pyautogui pynput
```
### Download ChromeDriver

Download the ChromeDriver from ChromeDriver - WebDriver for Chrome that matches your Chrome version. Extract the chromedriver.exe file and place it in a known directory.

### Update Script Path

In the Python script, update the executable_path in the webdriver.Chrome(executable_path="chromedriver.exe") line to the path where you placed your chromedriver.exe.

### Running the Script
To run the script, navigate to the directory containing the script in your terminal or command prompt and execute:

```bash
python snake_game_automation.py
```
