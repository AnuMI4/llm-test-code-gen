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

    "Button": """
    
"""
}
