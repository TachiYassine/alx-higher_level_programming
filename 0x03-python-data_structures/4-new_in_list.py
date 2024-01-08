def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return None
    if idx >= len(copy):
        return None
    copy[idx] = element
    return copy
