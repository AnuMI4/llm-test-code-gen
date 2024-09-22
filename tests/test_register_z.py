
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test1():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    
    first_name.send_keys("John")
    last_name.send_keys("Doe")
    username.send_keys("johndoe")
    password.send_keys("password123")
    
    register = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    register.click()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.success")))
    success = driver.find_element(By.CSS_SELECTOR, "h2.success")
    assert "Registration successful" in success.text
    
def test2():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    
    first_name.send_keys("!@#$%^&*()_+-={}[]|\:;'<>,./~")
    last_name.send_keys("Doe")
    username.send_keys("johndoe")
    password.send_keys("password123")
    
    register = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    register.click()
    
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.error")))
    error = driver.find_element(By.CSS_SELECTOR, "h2.error")
    assert "Please enter valid First Name" in error.text
    
def test3():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/register")
    time.sleep(2)
    
    cancel = driver.find_element(By.CSS_SELECTOR, "a.cancel")
    cancel.click()
    
    WebDriverWait(driver, 5).until(EC.url_contains("http://localhost:3000/login"))
    assert "http://localhost:3000/login" in driver.current_url
