def move(fn):
    def sorted(fn):
        fn.sort(key=lambda i: i >= 0)
    return sorted


@move
def move_negative_numbers_to_start_of_list(list):
    if (type(list) is type([])):
        return list
    else:
        raise AttributeError(f"Argument must be of type list, not {type(list)}")