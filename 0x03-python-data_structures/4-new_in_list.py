def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(copy):
        return my_list
    copy[idx] = element
    return copy
