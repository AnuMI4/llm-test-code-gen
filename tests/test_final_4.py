from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_case_1():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    inputElement = driver.find_element(By.NAME, "firstName")
    inputElement.send_keys("John")
    assert "John" in inputElement.get_attribute("value")

def test_case_2():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    inputElement = driver.find_element(By.NAME, "lastName")
    inputElement.send_keys("Doe")
    assert "Doe" in inputElement.get_attribute("value")

def test_case_3():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        link.click()
        assert 200 == driver.current_url.status_code
        assert "http://localhost:3000/login" == driver.current_url.geturl()