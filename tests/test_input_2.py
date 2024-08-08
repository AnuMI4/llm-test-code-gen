
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

def test_register(driver):
    driver.get("https://www.example.com/register")

    # Fill out first name field
    first_name = driver.find_element_by_id("first-name")
    fake = Faker()
    first_name.send_keys(fake.first_name())

    # Fill out last name field
    last_name = driver.find_element_by_id("last-name")
    last_name.send_keys(fake.last_name())

    # Fill out email field
    email = driver.find_element_by_id("email")
    email.send_keys(fake.safe_email())

    # Fill out password field
    password = driver.find_element_by_id("password")
    password.send_keys("MyStr0ngP@ssw0rd!")

    # Click register button
    register = driver.find_element_by_class_name("register-button")
    register.click()

if __name__ == "__main__":
    driver = webdriver.Firefox()
    test_register(driver)
    driver.quit()