import csv

# Function to load test cases from CSV
def load_test_cases(csv_file_path):
    test_cases = []
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_case = {
                "ID": row["Test case ID"],
                "Description": row["Description"],
                "Steps": row["Steps"],
                "Expected Result": row["Expected Result"]
            }
            test_cases.append(test_case)
    return test_cases
