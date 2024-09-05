from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the driver
# driver = webdriver.Chrome()

# # Navigate to the website
# driver.get("http://localhost:3000/register")
# time.sleep(2)

def test_case1():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)

    # Enter valid data on first name field
    driver.find_element(By.NAME, 'firstName').send_keys('John')
    
    # Enter valid data on last name field
    driver.find_element(By.NAME, 'lastName').send_keys('Doe')
    
    # Enter valid data on username field
    driver.find_element(By.NAME, 'username').send_keys('johndoe123')
    
    # Enter valid data on password field
    driver.find_element(By.NAME, 'password').send_keys('abcdefg')
    
    # Click on Register button
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    time.sleep(3)
    
    # Verify user can register successfully after entering correct data on first name, last name, username and password field
    assert driver.find_element(By.XPATH, "//div[@id='root']/div[2]/div").text == 'Registration successful'

    # Close the browser
    driver.quit()