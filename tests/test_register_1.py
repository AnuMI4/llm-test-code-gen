
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)

    # Enter valid username and password
    username = driver.find_element_by_name("username")
    username.send_keys("john")
    password = driver.find_element_by_name("password")
    password.send_keys("1234")

    # Click on login button
    login_button = driver.find_element_by_class_name("btn-primary")
    login_button.click()

    # Verify user is logged in successfully
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'You're logged in')]")))
    driver.quit()

def test_login_failure():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)

    # Enter invalid username and password
    username = driver.find_element_by_name("username")
    username.send_keys("invalid")
    password = driver.find_element_by_name("password")
    password.send_keys("123456789")

    # Click on login button
    login_button = driver.find_element_by_class_name("btn-primary")
    login_button.click()

    # Verify user is not logged in successfully
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Username or password is incorrect')]")))
    driver.quit()
