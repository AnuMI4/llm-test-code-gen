
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_register():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    # Step 1: Enter valid data on first name field
    first_name_input = driver.find_element(By.NAME, "firstName")
    first_name_input.send_keys("John")
    
    # Step 2: Enter valid data on last name field
    last_name_input = driver.find_element(By.NAME, "lastName")
    last_name_input.send_keys("Doe")
    
    # Step 3: Enter valid data on username field
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("johndoe")
    
    # Step 4: Enter valid data on password field
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Password123!")
    
    # Step 5: Click on Register button
    register_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    register_button.click()
    
    # Verify success message is displayed
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Registration successful')]")))
    
    driver.quit()
