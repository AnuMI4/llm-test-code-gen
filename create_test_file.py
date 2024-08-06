import os
def create_file_with_content(directory, filename, content):

    content = content.replace('`', '')

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w') as file:
        file.write(content)
    
    print(f"File created at: {file_path}")