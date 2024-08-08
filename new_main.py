from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from setup import setup
from load_json_file import load_json_file
from zero_shot_prompts import html_testing_prompts

url = load_json_file('regPage')

# Fetch url of the webpage
driver = setup(url)

# Extract input elements
input_elements = driver.find_elements(By.TAG_NAME, "input")
for elem in input_elements:
    print(f'{elem}\n')

input_elem_str = ", ".join([f'"{elem}"' for elem in input_elements])

# Generate a test file under test folder for testing these links
prompt =  html_testing_prompts["Input_field"].format(input_field_list=input_elem_str)
# generated_code = generate_test_case(prompt)

# directory = "tests"
# filename = "test_input_2.py"
# content = generated_code

# create_file_with_content(directory, filename, content)

driver.quit()
