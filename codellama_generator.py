import ollama

def generate_test_case(prompt):
    response = ollama.generate(model='codellama',
    prompt=prompt)
    return response['response']