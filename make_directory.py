import os

def make_node(public_key):
    public_key = public_key.replace("/", "")
    directory_path = f"nodes/{public_key}"
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' created successfully")

def check_node_availability(public_key):
    public_key = public_key.replace("/", "")
    directory_path = f"nodes/{public_key}"
    return os.path.isdir(directory_path)
