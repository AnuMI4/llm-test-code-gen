
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_phone_field():
    driver = webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/social-registration-form/")
    driver.maximize_window()
    time.sleep(2)
    phone_input = driver.find_element(By.ID, "phone_1623133256")
    print("Element is visible? " + str(phone_input.is_enabled()))
    phone_input.click()
    time.sleep(2)
    phone_input.send_keys("1234567890")
    # assert phone_input.get_attribute("value") == "1234567890"
    # driver.quit()

def test_incorrect_phone_format():
    driver = webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/social-registration-form/")
    time.sleep(2)
    phone_input = driver.find_element(By.ID, "phone_1623133256")
    phone_input.send_keys("abcdefghijklmnopqrstuvwxyz")
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Please provide a valid value for Phone.')]")))
    assert error_message.is_displayed()
    driver.quit()
