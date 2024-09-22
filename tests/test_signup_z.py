
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_case1():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/anumi/Documents/odin-sign-up-form/index.html")
    time.sleep(2)

    # Enter valid data on the First Name field
    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("John")

    # Enter valid data on the Last Name field
    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Smith")

    # Enter valid data on the Email field
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("john@company.com")

    # Enter invalid data on the Phone Number field e.g. less than 10 numbers
    phone_number_input = driver.find_element(By.ID, "phone")
    phone_number_input.send_keys("1234567890")

    # Enter valid data on the Password field
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Password123!")

    # Enter valid data on the Confirm Password field
    confirm_password_input = driver.find_element(By.ID, "confirm-password")
    confirm_password_input.send_keys("Password123!")

    # Click the Sign Up button
    sign_up_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign Up')]")
    sign_up_button.click()
    # time.sleep(2)

    # Verify error message is shown
    error_message = driver.find_element(By.ID, "error-message")
    assert error_message.is_displayed()

    driver.quit()
