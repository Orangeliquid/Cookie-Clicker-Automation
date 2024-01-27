from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_available_buyables(driver):
    """
    Clicks on the available buyable upgrade based on certain conditions.

    Parameters:
    - driver: WebDriver object for interacting with the web page.

    Returns:
    None
    """
    buyable_list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    top_buyable = None

    for buyable in buyable_list:
        if buyable.get_attribute("class") != "grayed":
            if buyable.get_attribute("id") != "":
                top_buyable = buyable.get_attribute("id")

    if top_buyable is not None:
        upgrade = driver.find_element(By.ID, top_buyable)
        upgrade.click()


def main():
    """
    Automates the process of clicking the cookie and checking for available upgrades.

    Parameters:
    None

    Returns:
    None
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

    # Time out info - this application is meant to see how many
    # cookies can be obtained in five minutes - thus duration_timer
    # is set to five minutes
    starting_time = time.time()
    timeout_sec = 5
    timeouts = 0
    duration_timer = starting_time + 60 * 5

    # Cookie object to click
    cookie_to_click = driver.find_element(By.ID, value="cookie")

    while time.time() < duration_timer:
        cookie_to_click.click()
        if time.time() >= starting_time + (timeout_sec * timeouts):
            get_available_buyables(driver)
            timeouts += 1
        time.sleep(0.01)  # Add a small delay between clicks


if __name__ == "__main__":
    main()
