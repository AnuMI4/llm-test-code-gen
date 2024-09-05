
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_phone_field_editable():
    driver = webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/social-registration-form/")
    time.sleep(2)

    phone_field = driver.find_element(By.ID, "phone_1623133256")
    phone_field.send_keys("1234567890")

    assert phone_field.get_attribute("value") == "1234567890"

    driver.quit()

def test_phone_field_error():
    driver = webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/social-registration-form/")
    time.sleep(2)

    phone_field = driver.find_element(By.ID, "phone_1623133256")
    phone_field.send_keys("abcdefghij")

    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Please provide a valid value for Phone.')]")

    assert error_message.is_displayed()

    driver.quit()
