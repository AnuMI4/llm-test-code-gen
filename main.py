import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content

# Fetch url of the webpage
with open('config.json', 'r') as f:
    config = json.load(f)
url = config['page2']

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Extract all links from the page
links = driver.find_elements(By.TAG_NAME, "a")
link_list = [link.get_attribute("href") for link in links]

driver.quit()

# Print the extracted links
print(link_list)

# Generate a test file under test folder for testing these links
prompt = f'Write test function in python to test the following array of links: {link_list} with assertion of response 200. Write different function with no parameters for each given link. Write code without explanation'
generated_code = generate_test_case(f'You are an expert programmer that writes simple, concise code. {prompt}')

directory = "tests"
filename = "test_4.py"
content = generated_code

create_file_with_content(directory, filename, content)
