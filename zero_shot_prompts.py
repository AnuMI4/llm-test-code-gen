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
For each test case, here is the corresponding element html, test case description, test steps, and expected result:
{test_cases_info}
Write code using Selenium.
Write each test as a function that corresponds to each test case. The function should have no parameters. The function does not need to be called.
Use Chromedriver but no need to provide path to Chromedriver.
Write code without explanation.
Don't write a main method.
"""
}
