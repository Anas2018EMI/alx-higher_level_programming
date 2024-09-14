#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = []
    for num in my_list:
        lst.append(num)

    if idx < 0:
        return lst

    if idx >= len(my_list):
        return lst

    lst[idx] = element
    return lst
