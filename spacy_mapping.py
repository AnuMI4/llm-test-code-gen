import spacy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from keyword_ext import ext_noun

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def get_element_text_with_label(driver, element):
    element_id = element.get_attribute("id")
    element_name = element.get_attribute("name")
    element_text = " ".join([
        element.get_attribute("name") or "",
        element.get_attribute("id") or "",
        element.get_attribute("placeholder") or "",
        element.get_attribute("type") or "",
        element.get_attribute("data-label") or ""
    ])

    # Initialize the label variable
    label_text = None

    # Check if a label exists for this element by id
    if element_id:
        try:
            label = driver.find_element(By.XPATH, f"//label[@for='{element_id}']")
            if label:
                label_text = label.text.strip()
                print(f"Label found by id: {label_text}")
                element_text = f"{label_text} {element_text}"
        except Exception:
            pass  # Continue to the next check if label is not found

    # Check if a label exists for this element by name if not found by id
    if not label_text and element_name:
        try:
            # Using contains to find label that might have different text formats
            # Look for labels where for attribute matches the element name
            label = driver.find_element(By.XPATH, f"//label[@for='{element_name}']")
            if label:
                label_text = label.text.strip()
                print(f"Label found by name: {label_text}")
                element_text = f"{label_text} {element_text}"
        except Exception:
            pass  # Continue if label is still not found

    print(f"Element Text with Label: {element_text}")
    return element_text

def match_test_case_to_element_spacy(test_case_description, elements, driver):
    best_match = None
    highest_similarity = 0

    # Process the test case description with spaCy
    ext_keyword_element_text = ext_noun(test_case_description)
    print(f'HELLO: {ext_keyword_element_text}')
    doc1 = nlp(ext_keyword_element_text)

    for element in elements:
        element_text = ""

        # Check if the element is an input field
        if element.tag_name == "input":
            # Get element text with label (from the helper function)
            element_text = get_element_text_with_label(driver, element)
        
        # Check if the element is a link (anchor tag)
        elif element.tag_name == "a":
            # Get the href attribute of the link
            element_text = 'links link'
        
        print(f"Element Text: {element_text}")

        # Process the element attributes with spaCy
        doc2 = nlp(element_text)
        
        # Calculate the similarity between the test case description and the element attributes
        similarity = doc1.similarity(doc2)

        # Keep track of the best match based on the highest similarity score
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = element

    return best_match, highest_similarity


def calc_sim(driver, elements_list, test_cases):
    # Extract input elements from the web page
    elements = elements_list

    # Dictionary to store the mapping of test case descriptions to elements
    test_case_to_element_mapping = {}

    for test_case in test_cases:
        description = test_case["Description"]
        matched_element, similarity = match_test_case_to_element_spacy(description, elements, driver)
        if matched_element:
            # Store the test case description and the HTML of the matched element
            test_case_to_element_mapping[description] = matched_element.get_attribute('outerHTML')

    return test_case_to_element_mapping
