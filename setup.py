from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def setup (url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(1)
    return driver
