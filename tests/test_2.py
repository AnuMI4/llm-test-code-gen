from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_last_name():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    input_field = driver.find_element(By.NAME, 'lastName')
    input_field.send_keys("John Doe")
    time.sleep(2)
    assert "John Doe" in input_field.get_attribute('value')
    driver.quit()