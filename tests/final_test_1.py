from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
class TestRegistration(unittest.TestCase):
    def test_register(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("http://localhost:3000/register")
        time.sleep(2)
        inputElement = driver.find_element(By.NAME, "lastName")
        inputElement.send_keys("Test User")
        time.sleep(2)
        self.assertEqual(inputElement.get_attribute("value"), "Test User")
if __name__ == '__main__':
    unittest.main()