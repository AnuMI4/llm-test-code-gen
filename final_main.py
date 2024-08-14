from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from setup import setup
from load_json_file import load_json_file
from zero_shot_prompts import html_testing_prompts
from few_shot_prompts import html_testing_prompts_few_shot
from csv_reader import load_test_cases
from spacy_mapping import calc_sim
from format_test_cases import format_test_cases

# Load the test cases
csv_file_path = './testcases/phone_test_case.csv'
test_cases_list = load_test_cases(csv_file_path)
print(test_cases_list)

# url of web page to test
url = load_json_file('demoRegForm')

# Fetch url of the webpage
driver = setup(url)

# Extract the following elements in page: Link, Form: Input fields, buttons
links = driver.find_elements(By.TAG_NAME, "a")
input_elements = driver.find_elements(By.TAG_NAME, "input")

combined_list = links + input_elements

mappings = calc_sim(driver, combined_list, test_cases_list)
print(f'this is mapping{mappings}')

list_elements = list(mappings.values())

test_cases_info = format_test_cases(test_cases_list, list_elements)

# list_elements_str = ", ".join([f'"{elem}"' for elem in list_elements])
# print(list_elements_str)

prompt = html_testing_prompts["generate_code"].format(url=url, test_cases_info=test_cases_info)
print('PROMPT'+prompt)
generated_code = generate_test_case(prompt)

directory = "tests"
filename = "test_final_6.py"
content = generated_code

create_file_with_content(directory, filename, content)

driver.quit()