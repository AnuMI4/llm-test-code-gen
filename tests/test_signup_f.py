from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_invalid_phone_number():
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/anumi/Documents/odin-sign-up-form/index.html")
    time.sleep(2)

    # Enter valid data on the First Name field
    driver.find_element(By.ID, "first-name").send_keys("John")

    # Enter valid data on the Last Name field
    driver.find_element(By.ID, "last-name").send_keys("Smith")

    # Enter valid data on the Email field
    driver.find_element(By.ID, "email").send_keys("john@company.com")

    # Enter invalid data on the Phone Number field e.g. less than 10 numbers
    driver.find_element(By.ID, "phone").send_keys("0123456789")

    # Enter valid data on the Password field
    driver.find_element(By.ID, "password").send_keys("Johnsmith12")

    # Enter valid data on the Confirm Password field
    driver.find_element(By.ID, "confirm-password").send_keys("Johnsmith12")

    # Click the Sign Up button
    driver.find_element(By.XPATH, "//*[contains(text(), 'Sign Up')]").click()

    # Verify user is not able to sign up with invalid phone number
    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Please enter a valid phone number, example: 012345678901')]").text
    assert error_message == "Please enter a valid phone number, example: 012345678901"

    driver.quit()