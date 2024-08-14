# Convert test cases data to test_cases_info
def format_test_cases(test_cases, elements):
    test_cases_info = ""
    for index, test_case in enumerate(test_cases):
        # Safely access the element at the current index
        element = elements[index] if index < len(elements) else "N/A"
        description = test_case.get("Description", "N/A")
        steps = test_case.get("Steps", "N/A")
        expected_result = test_case.get("Expected Result", "N/A")
        
        test_cases_info += f"Test Case {index + 1}:\n"
        test_cases_info += f"Element: {element}\n"
        test_cases_info += f"Test Case Description: {description}\n"
        test_cases_info += f"Test Steps: {steps}\n"
        test_cases_info += f"Expected Result: {expected_result}\n\n"
        
    return test_cases_info.strip()
