html_testing_prompts = {
    "Link": """
    Write test function in python to test the following array of links: {link_list}. 
    Assert that response for each should be 200. 
    Write different function for each given link with no parameters so it is runnable as a test. 
    Write code without explanation""",
       
    "Input_field": """
    Write test in python to test the following input elements in register page: {input_field_list}.
    If input field is first or last name field, use faker package to generate first or last name and enter it into input field.
    If input field is a username field, use faker package to generate first or last name and enter it into input field.""",
    
"generate_code": """
You will write test code in Python for the test cases provided to you.
Here is the URL of the page to test: {url}.
These are the provided test cases where for each test step in a test case, there is the corresponding element html, and the test case description and expected result are also provided:
{test_cases_info}\n
Write code using Selenium.
Write each test as a function that corresponds to each test case. The function should have no parameters. Do not call the function.
Use Chromedriver but no need to provide path to Chromedriver.
Add a little wait of around 2 seconds to allow the page to load after navigating to the URL.
Just write code do not write any explanation.
Don't write a main method.
Don't write any code outside the function except imports.
Note: For elements whose locators are not provided like success and error messages use By.XPATH, "//*[contains(text().
""",

"generate_code_with_example": """

You will write test code in Python for the test cases provided to you using Selenium.

Here is the URL of the page to test: {url}.

Below are the provided test cases. Each test case includes a description, the HTML element information for each test step, and the expected result:
{test_cases_info}

Instructions:
- Write the test code in Python using Selenium.
- Each test case should be written as a separate function. The function should have no parameters.
- Do not call any functions within the code.
- Use Chromedriver, but there is no need to provide the path to Chromedriver.
- Add a wait time of approximately 2 seconds after navigating to the URL to allow the page to load.
- Do not write a main method.
- Do not write any code outside the functions except for necessary imports.
- For elements without provided locators (such as success or error messages), use `By.XPATH` with a syntax similar to `"//*[contains(text(), 'desired text')]"`.
- Write code only. Don't write any explanation.
- Every function should have driver.quit().
- Use waits where appropirate e.g. to wait for page to load or element to be visible. 

Below is a template to help you complete the code by filling in the masked parts:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# [MASK] Add more imports if necessary

def [MASK]():  # Name function appropriately
    driver = webdriver.Chrome()
    driver.get("{url}")  # [MASK] Replace with provided URL
    time.sleep(2)  # Wait for the page to load

    # [MASK] Write code to locate elements and perform actions
    # Example:
    # driver.find_element(By.ID, "element_id").click()

    # [MASK] Write assertions based on expected results

    driver.quit()

Note: Write code only. Don't write any explanation.
"""
}
