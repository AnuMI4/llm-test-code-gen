from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from setup import setup
from load_json_file import load_json_file

url = load_json_file('regPage')

# Fetch url of the webpage
driver = setup(url)

# Extract input elements
input_elements = driver.find_elements(By.TAG_NAME, "input")

input_element_html = input_elements[0].get_attribute("outerHTML")

print(f'These are the input elements\n {input_element_html}')

# Generate a test file under test folder for testing these links
prompt = f'write a function in python selenium to test this element: {input_element_html}. Use faker package to generate and enter data into this element. Write code without explanation.'
generated_code = generate_test_case(prompt)

directory = "tests"
filename = "test_input_1.py"
content = generated_code

create_file_with_content(directory, filename, content)

driver.quit()
