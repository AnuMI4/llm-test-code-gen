from selenium.webdriver.common.by import By
from codellama_generator import generate_test_case
from create_test_file import create_file_with_content
from setup import setup
from load_json_file import load_json_file
from zero_shot_prompts import html_testing_prompts
from few_shot_prompts import html_testing_prompts_few_shot
from csv_reader import load_test_cases

# Load the test cases
csv_file_path = './testcases/test_cases.csv'
test_cases_list = load_test_cases(csv_file_path)
test_cases_str = "\n".join(test_cases_list)

# url of web page to test
url = load_json_file('regPage')

# Fetch url of the webpage
driver = setup(url)

# Extract the following elements in page: Link, Form: Input fields, buttons
links = driver.find_elements(By.TAG_NAME, "a")
link_list = [link.get_attribute("href") for link in links]
input_elements = driver.find_elements(By.TAG_NAME, "input")

# Convert the list to a string representation suitable for the prompt
link_list_str = ", ".join([f'"{link}"' for link in link_list])
input_elem_str = ", ".join([f'"{elem}"' for elem in input_elements])

prompt = html_testing_prompts_few_shot["Input_field"].format(test_cases=test_cases_str, elements=input_elem_str + link_list_str)
generated_code = generate_test_case(prompt)

directory = "tests"
filename = "final_test_1.py"
content = generated_code

create_file_with_content(directory, filename, content)

driver.quit()