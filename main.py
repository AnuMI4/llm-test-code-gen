from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from setup import setup
from load_json_file import load_json_file
from prompts import html_testing_prompts
from csv_reader import load_test_cases
from spacy_mapping import calc_sim
from format_test_cases import format_test_cases

# Load the test cases
csv_file_path = './testcases/login_test_cases.csv'
test_cases_list = load_test_cases(csv_file_path)
# print(test_cases_list)

# url of web page to test
# direct url can also be provided here instead of using load_json_file(url)
# url = http://localhost:3000/register
url = load_json_file('loginPage')

# Fetch url of the webpage
driver = setup(url)

# Extract the following elements in page: Link, Input fields, buttons
links = driver.find_elements(By.TAG_NAME, "a")
input_elements = driver.find_elements(By.TAG_NAME, "input")
button_elements = driver.find_elements(By.TAG_NAME, "button")

combined_list = links + input_elements + button_elements

mappings = calc_sim(driver, combined_list, test_cases_list)
# print(f'this is mapping{mappings}')

list_elements = [item['element_html'] for sublist in mappings.values() for item in sublist]

test_cases_info = format_test_cases(test_cases_list, list_elements)
print(test_cases_info)

prompt = html_testing_prompts["generate_code_with_example"].format(url=url, test_cases_info=test_cases_info)
print('PROMPT'+prompt)
generated_code = generate_test_case(prompt)

directory = "tests"
filename = "test_register_1.py"
content = generated_code

create_file_with_content(directory, filename, content)

driver.quit()