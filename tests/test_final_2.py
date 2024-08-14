import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_last_name_field(self):
        driver = self.driver
        driver.get("http://localhost:3000/register")
        last_name = driver.find_element_by_name("lastName")
        last_name.send_keys("John")
        self.assertEqual(last_name.get_attribute("value"), "John")

    def test_first_name_field(self):
        driver = self.driver
        driver.get("http://localhost:3000/register")
        first_name = driver.find_element_by_name("firstName")
        first_name.send_keys("Doe")
        self.assertEqual(first_name.get_attribute("value"), "Doe")

    def test_cancel_link(self):
        driver = self.driver
        driver.get("http://localhost:3000/register")
        cancel_link = driver.find_element_by_link_text("Cancel")
        cancel_link.click()
        self.assertEqual(driver.current_url, "http://localhost:3000/login")

    def tearDown(self):
        self.driver.quit()