
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)
    
    # Enter valid username "john" on username field
    username_input = driver.find_element(By.XPATH, "//*[contains(text(), 'Username')]")
    username_input.send_keys("john")
    
    # Enter valid password "1234" on password field
    password_input = driver.find_element(By.XPATH, "//*[contains(text(), 'Password')]")
    password_input.send_keys("1234")
    
    # Click on Login button
    login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    login_button.click()
    
    # Verify user can login successfully after entering correct username and password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'You're logged in')]")))
    print("User is logged in successfully")
    
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/login")
    time.sleep(2)
    
    # Enter valid username "john" on username field
    username_input = driver.find_element(By.XPATH, "//*[contains(text(), 'Username')]")
    username_input.send_keys("john")
    
    # Enter valid password "1234" on password field
    password_input = driver.find_element(By.XPATH, "//*[contains(text(), 'Password')]")
    password_input.send_keys("invalid_password")
    
    # Click on Login button
    login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    login_button.click()
    
    # Verify user cannot login successfully with incorrect username and password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Username or password is incorrect')]")))
    print("User cannot log in with invalid credentials")
