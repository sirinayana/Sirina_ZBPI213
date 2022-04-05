def bin_search(li, element):
    first_part = -1
    second_part = len(li)
    while second_part > first_part + 1:
        middle = (first_part + second_part) // 2
        if li[middle] >= element:
            second_part = middle
        else:
            first_part = middle
    if second_part < len(li) and li[second_part] == element:
        return second_part
    return -1

