from selenium import webdriver
import time

def phone_field():
    driver=webdriver.Chrome()
    driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")
    time.sleep(3)
    inputElement = driver.find_element_by_id("phone_1665627880")
    inputElement.send_keys("1234567890")
    assert "1234567890" in inputElement.get_attribute("value")

phone_field()