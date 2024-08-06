import json

def load_json_file (file):
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config[file]