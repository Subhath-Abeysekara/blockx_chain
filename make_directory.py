import os
import shutil

import env


def copy_chain_to_node(public_key):
    dir_list = os.listdir("nodes")
    dir_list.remove(public_key)
    blocks = os.listdir(f"nodes/{dir_list[0]}")
    print(blocks)
    for block in blocks:
        source_file = f'nodes/{dir_list[0]}/{block}'
        destination_directory = f'nodes/{public_key}'
        shutil.copy(source_file, destination_directory)


def make_node(public_key):
    public_key = public_key.replace("/", "")
    directory_path = f"nodes/{public_key}"
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' created successfully")
    copy_chain_to_node(public_key)

def make_system_node():
    public_key = env.system_account.replace("/", "")
    directory_path = f"nodes/{public_key}"
    if not os.path.isdir(directory_path):
        os.mkdir(directory_path)
        print(f"Directory '{directory_path}' created successfully")

def check_node_availability(public_key):
    public_key = public_key.replace("/", "")
    directory_path = f"nodes/{public_key}"
    return os.path.isdir(directory_path)