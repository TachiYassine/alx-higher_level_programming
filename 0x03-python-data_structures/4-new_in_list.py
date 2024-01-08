def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return copy
    if idx >= len(copy):
        return copy
    copy[idx] = element
    return copy
