def substring_slice(path2file_1, path2file_2):
    with open(path2file_1, encoding='utf-8') as file:
        result = [i.strip() for i in file.readlines()]
    with open(path2file_2, encoding='utf-8') as file:
        current_line = 0
        for line in file.readlines():
            index1, index2 = [int(i) for i in line.split()]
            result[current_line] = result[current_line][index1:index2 + 1]
            current_line += 1
    return ' '.join(result)

