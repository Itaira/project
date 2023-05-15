import time
import json
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Testing functions
def start_selenium(user_id, xpath):
    # Declare the selenium web driver
    driver = webdriver.Chrome(service=Service("/Users/itairaviv/Downloads/chromedriver_mac_arm64/chromedriver"))
    driver.implicitly_wait(10)  # Wait max 10 seconds to find element
    driver.get(f"http://localhost:5001/users/get_user_data/{user_id}")  # Open the driver on flask server

    # Define the locator for the user name element
    locator = (By.XPATH, xpath)
    return driver, locator


def check_element_exists_testing(driver, locator):
    try:
        element = driver.find_element(*locator)
        print("SUCCESS: User name element exists.", element)  # If the element is found, print a success message
    except NoSuchElementException:
        print(
            "ERROR: User name element is not showing.")  # If the element is not visible within the specified time, print an error message


def check_element_visible_testing(driver, locator):
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator))  # Wait for the user name element to be visible
        print("SUCCESS: User name element is showing.")  # If the element is visible, print a success message
    except TimeoutException:
        print(
            "ERROR: User name element is not showing.")  # If the element is not visible within the specified time, print an error message


def print_connection_testing(driver):
    print("Url connection:", driver.current_url)  # Current url returns the current url connected to
    print("Driver name:", driver.name)
    return 0


def print_user_testing(driver, locator):
    try:
        element = driver.find_element(*locator)
        user_name = json.loads(element.text)['user_name'][0]
        print("SUCCESS: User name found:", user_name)  # If the element is found, print a success message
    except NoSuchElementException:
        print(
            "ERROR: User name element is not showing.")  # If the element is not visible within the specified time, print an error message
        exit(1)


# # TESTING SEQUENCE WITH TESTING VALUES
# user_id = "999"
# xpath = "/html/body/pre"
#
# driver, locator = start_selenium(user_id, xpath)
# print_connection_testing(driver)
# time.sleep(2)
# check_element_exists_testing(driver, locator)
# time.sleep(2)
# print_user_testing(driver, locator)
#
# # Quit the WebDriver
# driver.quit()
