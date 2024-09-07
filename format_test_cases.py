def format_test_cases(test_cases, elements):
    test_cases_info = ""
    element_index = 0

    for index, test_case in enumerate(test_cases):
        description = test_case.get("Description", "N/A")
        steps = test_case.get("Steps", "").split('\n')
        expected_result = test_case.get("Expected Result", "N/A")

        num_steps = len(steps)
        num_elements = len(elements)

        # Ensure the steps and elements match
        if num_steps > num_elements:
            print(f"Warning: There are more steps ({num_steps}) than elements ({num_elements}).")

        # Loop through each step and match with elements
        for step_index, step in enumerate(steps):
            if element_index < num_elements:
                element = elements[element_index]
            else:
                element = "N/A"  # Handle case where there are more steps than elements
            test_cases_info += f"Test Case {index + 1}:\n"
            test_cases_info += f"Step: {step}\n"
            test_cases_info += f"Element: {element}\n\n"
            element_index += 1
        
        # Add description and expected result after listing all steps
        test_cases_info += f"Test Case Description: {description}\n"
        test_cases_info += f"Expected Result: {expected_result}\n\n"
        
    return test_cases_info.strip()
