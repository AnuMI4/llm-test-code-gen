
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_register_success():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    # Enter valid data on first name field
    driver.find_element(By.NAME, "firstName").send_keys("John")
    
    # Enter valid data on last name field
    driver.find_element(By.NAME, "lastName").send_keys("Doe")
    
    # Enter valid data on username field
    driver.find_element(By.NAME, "username").send_keys("johndoe123")
    
    # Enter valid data on password field
    driver.find_element(By.NAME, "password").send_keys("Password123!")
    
    # Click on Register button
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(1)
    
    # Verify user can register successfully after entering correct data on first name, last name, username and password field
    assert "Registration successful" in driver.page_source
    
    driver.quit()

def test_register_failure():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    # Enter invalid data on first name field like special characters
    driver.find_element(By.NAME, "firstName").send_keys("!@#$%^&*()_+")
    
    # Enter valid data on last name field
    driver.find_element(By.NAME, "lastName").send_keys("Doe")
    
    # Enter valid data on username field
    driver.find_element(By.NAME, "username").send_keys("johndoe123")
    
    # Enter valid data on password field
    driver.find_element(By.NAME, "password").send_keys("Password123!")
    
    # Click on Register button
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(1)
    
    # Verify user cannot register successfully after entering incorrect data on first name
    assert "Please enter valid First Name" in driver.page_source
    
    driver.quit()

def test_cancel():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    # Click on the Cancel link
    driver.find_element(By.CSS_SELECTOR, ".btn-link").click()
    
    # Verify when the Cancel link is clicked, user is redirected to the login page
    assert "/login" in driver.current_url
    
    driver.quit()
