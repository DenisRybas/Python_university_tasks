def move_negative_numbers_to_start_of_list(list):
    if type(list) is type([]):
        l = len(list)
        iterator1 = iter(list)
        iterator2 = iter(list)
        for i in range(l):
            element = next(iterator1)
            if element < 0:
                list.append(element)
        for i in range(l):
            element = next(iterator2)
            if element >= 0:
                list.append(element)
        del list[:l]
    else:
        raise TypeError(f"Argument must be of type list, not {type(list)}")