from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)
    
    # Enter valid username "john" on username field
    user_name_field = driver.find_element(By.NAME, "username")
    user_name_field.send_keys("john")
    
    # Enter valid password "1234" on password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("1234")
    
    # Click on Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    login_button.click()
    time.sleep(1)
    
    # Verify user can login successfully after entering correct username and password
    success_message = driver.find_element(By.XPATH, '//*[contains(text(), "You\'re logged in")]')
    assert success_message.is_displayed()
    
    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)
    
    # Enter valid username "john" on username field
    user_name_field = driver.find_element(By.NAME, "username")
    user_name_field.send_keys("john")
    
    # Enter invalid password "12345" on password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("12345")
    
    # Click on Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    login_button.click()
    time.sleep(1)
    
    # Verify user cannot login successfully with incorrect username and password
    error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Username or password is incorrect')]")
    assert error_message.is_displayed()
    
    driver.quit()
    