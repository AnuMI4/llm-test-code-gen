"""register test file"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register():
    """run register test"""
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)

    # Enter valid data on first name field
    driver.find_element(By.NAME, "firstName").send_keys("John")

    # Enter valid data on last name field
    driver.find_element(By.NAME, "lastName").send_keys("Doe")

    # Enter valid data on username field
    driver.find_element(By.NAME, "username").send_keys("johndoe")

    # Enter valid data on password field
    driver.find_element(By.NAME, "password").send_keys("abc123")

    # Click on Register button
    driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]").click()

    # Assert that the success message is displayed
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Registration successful')]").is_displayed()

    driver.quit()
