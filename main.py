from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Time out info
starting_time = time.time()
timeout_sec = 5
timeouts = 0
five_min = starting_time + 60 * 5

# Cookie object to click
cookie_to_click = driver.find_element(By.ID, value="cookie")


# Function to get available upgrades
def get_available_buyables():
    buyable_list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    top_buyable = None

    for buyable in buyable_list:
        if buyable.get_attribute("class") != "grayed":
            if buyable.get_attribute("id") != "":
                top_buyable = buyable.get_attribute("id")

    if top_buyable is not None:
        upgrade = driver.find_element(By.ID, top_buyable)
        upgrade.click()


while time.time() < five_min:
    cookie_to_click.click()
    if time.time() >= starting_time + (timeout_sec * timeouts):
        get_available_buyables()
        timeouts += 1
    time.sleep(0.01)  # Add a small delay between clicks

