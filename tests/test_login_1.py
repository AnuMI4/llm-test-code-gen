
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_successful():
    
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(4)

    # Enter valid username "john" on username field
    driver.find_element(By.NAME, "username").send_keys("john")

    # Enter valid password "1234" on password field
    driver.find_element(By.NAME, "password").send_keys("1234")

    # Click on Login button
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    time.sleep(2)

    # Assert that the success message is displayed
    assert driver.find_element(By.XPATH, '//*[contains(text(), "You are logged in")]')

def test_login_unsuccessful():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)

    # Enter valid username "john" on username field
    driver.find_element(By.NAME, "username").send_keys("john")

    # Enter invalid password "1234" on password field
    driver.find_element(By.NAME, "password").send_keys("abcdefg")

    # Click on Login button
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    time.sleep(1)

    # Assert that the error message is displayed
    assert driver.find_element(By.XPATH, '//*[contains(text(), "Username or password is incorrect")]')