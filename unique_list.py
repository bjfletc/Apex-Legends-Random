# module that generates a unique list out of a given list.

import random


def generate_unique_list(list_name: list, len_of_output_list: int):
    uni_list = []
    ran_item = random.randint(0, len(list_name) - 1)

    for i in range(0, len_of_output_list):
        while ran_item in uni_list:
            ran_item = random.randint(0, len(list_name) - 1)

        uni_list.append(ran_item)
    return uni_list
