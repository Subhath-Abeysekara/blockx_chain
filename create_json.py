import os
import json
from pathlib import Path

# Example JSON data
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"]
}


def count_files_in_directory(directory_path):
    file_count = 0
    for _, _, files in os.walk(directory_path):
        file_count += len(files)

    return file_count

def save_json(data , genesis = False):
    dir_list = os.listdir("nodes")
    print(dir_list)
    if genesis:
        file_path = f"nodes/{dir_list[0]}/GenesisBlock.json"
        path = Path(file_path)
        if path.exists():
            print("GenesisBlock is available")
            return
    for dir in dir_list:
        directory_path = f"nodes/{dir}"
        num_files = count_files_in_directory(directory_path=directory_path)
        block_name = f'Block{num_files + 1}.json' if num_files > 0 else 'GenesisBlock.json'
        file_path = os.path.join(directory_path, block_name)
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON data has been written to {file_path}")
    return

