html_testing_prompts_few_shot = {
    "Link": """
    ### Instructions:
    # Write Python test functions for the given array of links. For each link, create a separate function that tests if the response status code is 200. Use the pattern shown in the examples below. Do not include explanations, only the code.

    # Example 1
    ### Input:
    Links: ["https://example1.com"]

    ### Output:
    import requests

    def test_link_1():
        response = requests.get("https://example1.com")
        assert response.status_code == 200


    # Example 2
    ### Input:
    Links: ["https://example2.com", "https://example3.com"]

    ### Output:
    import requests

    def test_link_1():
        response = requests.get("https://example2.com")
        assert response.status_code == 200

    def test_link_2():
        response = requests.get("https://example3.com")
        assert response.status_code == 200


    # Example 3
    ### Input:
    Links: ["https://example4.com", "https://example5.com", "https://example6.com"]

    ### Output:
    import requests

    def test_link_1():
        response = requests.get("https://example4.com")
        assert response.status_code == 200

    def test_link_2():
        response = requests.get("https://example5.com")
        assert response.status_code == 200

    def test_link_3():
        response = requests.get("https://example6.com")
        assert response.status_code == 200


    # New Task
    ### Input:
    Links: [{link_list}]

    ### Output:""",

    "Input_field": """
    ### Instructions:
write test code in python using selenium for the following test cases: {test_cases}
here are the elements html: {elements}
write each test case in a separate function with no parameters, so it is runnable as a test
write code without explanation

# Example 1
### Input:
URL: https://exampleURL.com
Elements: ["https://example1.com", "<selenium.webdriver.remote.webelement.WebElement (session="143a2d967232709277f1043e871ea30e", element="f.49B1C57617606F7D7D9C0AEF661E30AD.d.775EE8401E9E394C91B85C8AB669B332.e.3")>"]

### Output:
import requests
from faker import Faker
from selenium import webdriver

def test_link_1():
    response = requests.get("https://example1.com")
    assert response.status_code == 200

def test_input_1():
    driver = webdriver.Chrome()
    driver.get(https://exampleURL.com)
    name = fake.name()
    inputElement = driver.find_element(By.NAME, "exampleName")
    inputElement.send_keys(name)
    assert element.get_attribute('value') == name
    driver.quit()

# Example 2
### Input:
URL: https://exampleURL.com
Elements: ["https://example1.com", "https://example2.com", "<selenium.webdriver.remote.webelement.WebElement (session="143a2d967232709277f1043e871ea30e", element="f.49B1C57617606F7D7D9C0AEF661E30AD.d.775EE8401E9E394C91B85C8AB669B332.e.3")>, "<selenium.webdriver.remote.webelement.WebElement (session="143a2d967232709277f1043e871ea30e", element="f.49B1C57617606F7D7D9C0AEF661E30AD.d.775EE8401E9E394C91B85C8AB669B332.e.5")>"]

### Output:
import requests
from faker import Faker
from selenium import webdriver

def test_link_1():
    response = requests.get("https://example1.com")
    assert response.status_code == 200

def test_link_2():
    response = requests.get("https://example2.com")
    assert response.status_code == 200

def test_input_1():
    driver = webdriver.Chrome()
    driver.get(https://exampleURL.com)
    name = fake.name()
    inputElement = driver.find_element(By.NAME, "exampleName")
    inputElement.send_keys(name)
    assert inputElement.get_attribute('value') == name
    driver.quit()

def test_input_2():
    driver = webdriver.Chrome()
    driver.get(https://exampleURL.com)
    last_name = fake.last_name()
    inputElementLastName = driver.find_element(By.CLASS, "exampleClass")
    inputElementLastName.send_keys(last_name)
    assert inputElementLastName.get_attribute('value') == last_name
    driver.quit()
    
    """
}
