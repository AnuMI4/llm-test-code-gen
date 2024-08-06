
import time
from faker import Faker
from selenium import webdriver

fake = Faker()
# don't set path to chromedriver
# add url for web page on prompt
# write prompt as a series of steps
driver = webdriver.Chrome('path/to/chromedriver')
driver.get("https://example.com")

# Enter data into the firstName input field using faker package
first_name = fake.name()
last_name = fake.last_name()
full_name = first_name + " " + last_name
driver.find_element_by_css_selector("input[name='firstName']").send_keys(full_name)

# Verify that the input field is valid
if driver.find_element_by_css_selector("input[name='firstName']").is_valid():
    print("First name entered successfully!")
else:
    print("Error entering first name.")

driver.quit()
