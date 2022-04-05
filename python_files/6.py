def calculate(path2file):
    result = []
    with open(path2file, encoding='utf-8') as file:
        for line in file.readlines():
            l = [i.strip() for i in line.split()]
            l1, l2 = int(l[1]), int(l[2])
            if l[0] == '+':
                result.append(str(l1 + l2))
            elif l[0] == '-':
                result.append(str(l1 - l2))
            elif l[0] == '*':
                result.append(str(l1 * l2))
            elif l[0] == '//':
                result.append(str(l1 // l2))
            elif l[0] == '%':
                result.append(str(l1 % l2))
            elif l[0] == '**':
                result.append(str(l1 ** l2))
        return ','.join(result)

