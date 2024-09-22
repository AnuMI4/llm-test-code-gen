
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_registration():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)

    first_name_input = driver.find_element(By.NAME, "firstName")
    last_name_input = driver.find_element(By.NAME, "lastName")
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    register_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    username_input.send_keys("johndoe")
    password_input.send_keys("password123")
    register_button.click()
    time.sleep(1)

    # Check for success message
    success_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Registration successful')]")
    assert success_message.is_displayed()

    driver.quit()

def test_invalid_registration():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)

    first_name_input = driver.find_element(By.NAME, "firstName")
    last_name_input = driver.find_element(By.NAME, "lastName")
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    register_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    first_name_input.send_keys("John!@#$")
    last_name_input.send_keys("Doe")
    username_input.send_keys("johndoe")
    password_input.send_keys("password123")
    register_button.click()
    time.sleep(1)

    # Check for error message
    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Please enter valid First Name')]")
    assert error_message.is_displayed()

    driver.quit()