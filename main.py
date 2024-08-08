import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from zero_shot_prompts import html_testing_prompts
from few_shot_prompts import html_testing_prompts_few_shot

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

# Convert the list to a string representation suitable for the prompt
link_list_str = ", ".join([f'"{link}"' for link in link_list])

# Generate a test file under test folder for testing these links
prompt = html_testing_prompts_few_shot["Link"].format(link_list=link_list_str)
generated_code = generate_test_case(prompt)

directory = "tests"
filename = "test_6.py"
content = generated_code

create_file_with_content(directory, filename, content)
