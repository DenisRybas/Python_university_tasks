def move_negative_numbers_to_start_of_list(list):
    if (type(list) is type([])):
        list.sort(key=lambda i: i >= 0)
    else:
        raise TypeError(f"Argument must be of type list, not {type(list)}")
