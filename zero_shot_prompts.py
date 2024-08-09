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
You will write test code in Python.
Here is the url of the page to test: {url}.
Here is the element: {element}.
And here is the test case: {test_case}.
These are the test steps: {test_steps}.
And this is the Expected Result: {expected_result}.
Write code using Selenium.
Write this test as a function without parameters so it is runnable.
Use Chromedriver but no need to provide path to chromedriver.
Write code without explanation.
This code will be written to a directory that is configured as directory for running pytest tests so no need to write main method.
"""
}
