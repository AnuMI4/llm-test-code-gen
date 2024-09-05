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

    label_text = None

    if element_id:
        try:
            label = driver.find_element(By.XPATH, f"//label[@for='{element_id}']")
            if label:
                label_text = label.text.strip()
                element_text = f"{label_text} {element_text}"
        except Exception:
            pass

    if not label_text and element_name:
        try:
            label = driver.find_element(By.XPATH, f"//label[@for='{element_name}']")
            if label:
                label_text = label.text.strip()
                element_text = f"{label_text} {element_text}"
        except Exception:
            pass

    return element_text

def match_test_step_to_element_spacy(test_step_description, elements, driver):
    best_match = None
    highest_similarity = 0

    # Process the test step description with spaCy
    ext_keyword_element_text = ext_noun(test_step_description)
    doc1 = nlp(ext_keyword_element_text.lower())

    for element in elements:
        element_text = ""

        if element.tag_name == "input":
            element_text = get_element_text_with_label(driver, element)
        elif element.tag_name == "a":
            element_text = 'links link'
        elif element.tag_name == "button":
            element_text = 'button'

        doc2 = nlp(element_text.lower())
        similarity = doc1.similarity(doc2)

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = element

    return best_match, highest_similarity

def calc_sim(driver, elements_list, test_cases):
    elements = elements_list

    test_case_to_element_mapping = {}

    for test_case in test_cases:
        description = test_case["Description"]
        steps = test_case["Steps"].split("\n")  # Split the steps into individual steps

        step_mappings = []

        for step in steps:
            matched_element, similarity = match_test_step_to_element_spacy(step, elements, driver)
            if matched_element:
                step_mappings.append({
                    "step": step,
                    "element_html": matched_element.get_attribute('outerHTML'),
                    "similarity": similarity
                })

        test_case_to_element_mapping[description] = step_mappings

    return test_case_to_element_mapping
