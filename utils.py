import os 
import json


def load_json(file_path):
    """Load a JSON file and return its content."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as file:
        return json.load(file)
    

if __name__ == "__main__":
    file = os.path.join(os.path.dirname(__file__), 'data', '2023-11-01_2023-11-08.json')
    data = load_json(file)
    for key, value in data.items():
        print(f"{key}: {type(value)} {len(value)}")
        
