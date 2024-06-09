import os
import random


def select_nodes(public_key):
    dir_list = os.listdir("nodes")
    print(dir_list)
    dir_list.remove(public_key)
    print(dir_list)
    num_elements_to_pick = random.randint(2, len(dir_list))
    random_elements = random.sample(dir_list, num_elements_to_pick)
    print(num_elements_to_pick , random_elements)
    return {
        "state":True,
        "public_keys":random_elements
    }

# select_nodes(public_key="MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEaYNUaOK3oEV834c0xeA6RV7pHq8leVNrYgqWSHhUCABRUGrrCkMHQvnATljRKd5g+nW2REyuq5voTwkV2cKJrw==")