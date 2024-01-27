# Cookie Clicker Automation

## Overview
This Python script uses Selenium to automate the process of clicking on a cookie in the popular game "Cookie Clicker" and checking for available upgrades. The script opens the game in a Chrome browser, continuously clicks on the cookie, and periodically checks for available buyable upgrades.

## Requirements
Before running the script, make sure you have the following installed:
- Python 3
- Selenium library
- Chrome browser installed
- ChromeDriver (ensure it's in your system's PATH)


## Installation
1. Install the required libraries using the following command:
  ```bash
    pip install selenium
  ```
2. Download ChromeDriver from here and ensure it's in your system's PATH.

## Usage
1. Clone the repository or download the script.
  ```bash
    git clone https://github.com/Orangeliquid/cookie-clicker-automation.git
  ```
2. Navigate to the project directory.
  ```bash
    cd cookie-clicker-automation
  ```
3. Run the script using the following command:
  ```bash
    python cookie_clicker_automation.py
  ```
4. Sit back and watch the cookies pile up!

## Script Details
`get_available_buyables(driver)`
This function identifies and clicks on the available buyable upgrade based on certain conditions.

### Parameters:
- `driver`: WebDriver object for interacting with the web page.

### Returns:
- None

`main()`
This function automates the process of clicking the cookie and checking for available upgrades. It initializes a Chrome WebDriver, navigates to the Cookie Clicker game, and continuously clicks on the cookie. It periodically checks for available upgrades during a specified time duration (default is 5 minutes).

### Parameters:
- None

### Returns:
- None

## Note
-The script is set to run for 5 minutes by default. You can adjust the duration_timer variable in the main() function to change the runtime.

-Ensure that the Chrome browser is installed, and ChromeDriver is correctly set up in your system's PATH.

-The script uses a small delay between clicks (time.sleep(0.01)) to avoid overwhelming the browser.

-This script is designed for educational and entertainment purposes and should be used responsibly.

-Feel free to contribute to and modify the script as needed. Enjoy your automated Cookie Clicker experience!

## License
This project is licensed under the [MIT License](LICENSE.txt).
