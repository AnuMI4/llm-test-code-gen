import csv

# Function to load test cases from CSV
def load_test_cases(csv_file_path):
    test_cases = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_case_id = row["Test case ID"]
            description = row["Description"]
            steps = row["Steps"]
            expected_result = row["Expected Result"]
            test_cases.append(f"ID: {test_case_id}, Description: {description}, Steps: {steps}, Expected Result: {expected_result}")
    return test_cases
