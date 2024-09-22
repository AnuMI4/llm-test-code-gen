To setup and run this code, please follow the following steps:

Pre-requisites:
- Have Python 3 installed
- Have ollama installed (https://ollama.com/)
- Have Code Llama installed via Ollama (ollama run codellama)
- Have VS code installed
- Have Python extension installed

1) Install all the requirements using this command:
   ```pip install -r requirements.txt```
   
2) On main.py file, set the following variables:
   a) csv_file_path - this is the path to your test cases csv file, should contain test cases for the webpage to test
   b) url - this is the url of the webpage you want to test
   c) filename - this is the file generated with tests for the given url and test cases. It will be under the 'tests' directory.
   
3) Make sure to configure Pytest on tests directory so generated tests on file can be executed
