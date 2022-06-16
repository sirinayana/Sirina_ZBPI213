# задача 1
def fact(x):
    if x == 1:
        return x
    else:
        return x*fact(x-1)


# задача 2
def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))


# задача 3
def square(li):
    return list(map(lambda x: x ** 2, li))


# задача 4
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


# задача 5
def is_palindrome(string):
    s = string.lower()
    a, b = 0, len(string) - 1
    flag = "YES"
    while a < b:
        while not s[a].isalpha():
            a += 1
        while not s[b].isalpha():
            b -= 1
        if s[a] != s[b]:
            flag = "NO"
            break
        else:
            a += 1
            b -= 1
    return flag


# задача 6
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


# задача 7
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


# задача 8
def decode_ch(string_of_elements):
    periodic_table = {
    "Ac": "Актиний",
    "Ag": "Серебро",
    "Al": "Алюминий",
    "Am": "Америций",
    "Ar": "Аргон",
    "As": "Мышьяк",
    "At": "Астат",
    "Au": "Золото",
    "B": "Бор",
    "Ba": "Барий",
    "Be": "Бериллий",
    "Bh": "Борий",
    "Bi": "Висмут",
    "Bk": "Берклий",
    "Br": "Бром",
    "C": "Углерод",
    "Ca": "Кальций",
    "Cd": "Кадмий",
    "Ce": "Церий",
    "Cf": "Калифорний",
    "Cl": "Хлор",
    "Cm": "Кюрий",
    "Cn": "Коперниций",
    "Co": "Кобальт",
    "Cr": "Хром",
    "Cs": "Цезий",
    "Cu": "Медь",
    "Db": "Дубний",
    "Ds": "Дармштадтий",
    "Dy": "Диспрозий",
    "Er": "Эрбий",
    "Es": "Эйнштейний",
    "Eu": "Европий",
    "F": "Фтор",
    "Fe": "Железо",
    "Fl": "Флеровий",
    "Fm": "Фермий",
    "Fr": "Франций",
    "Ga": "Галий",
    "Gd": "Гадолиний",
    "Ge": "Германий",
    "H": "Водород",
    "He": "Гелий",
    "Hf": "Гафний",
    "Hg": "Ртуть",
    "Ho": "Гольмий",
    "Hs": "Хассий",
    "I": "Йод",
    "In": "Индий",
    "Ir": "Иридий",
    "K": "Калий",
    "Kr": "Криптон",
    "La": "Лантан",
    "Li": "Литий",
    "Lr": "Лоуренсий",
    "Lu": "Лютеций",
    "Lv": "Ливерморий",
    "Mc": "Московий",
    "Md": "Менделевий",
    "Mg": "Магний",
    "Mn": "Марганец",
    "Mo": "Молибден",
    "Mt": "Мейтнерий",
    "N": "Азот",
    "Na": "Натрий",
    "Nb": "Ниобий",
    "Nd": "Неодим",
    "Ne": "Неон",
    "Nh": "Нихоний",
    "Ni": "Никель",
    "No": "Нобелий",
    "Np": "Нептуний",
    "O": "Кислород",
    "Ods": "Пасхалочка",
    "Og": "Оганесон",
    "Os": "Осмий",
    "P": "Фосфор",
    "Pa": "Протактиний",
    "Pb": "Свинец",
    "Pd": "Палладий",
    "Pm": "Прометий",
    "Po": "Полоний",
    "Pr": "Празеодим",
    "Pt": "Платина",
    "Pu": "Плутоний",
    "Ra": "Радий",
    "Rb": "Рубидий",
    "Re": "Рений",
    "Rf": "Разерфордий",
    "Rg": "Ренгений",
    "Rh": "Родий",
    "Rn": "Радон",
    "Ru": "Рутений",
    "S": "Сера",
    "Sb": "Сурьма",
    "Sc": "Скандий",
    "Se": "Селен",
    "Sg": "Сиборгий",
    "Si": "Кремний",
    "Sm": "Самарий",
    "Sn": "Олово",
    "Sr": "Стронций",
    "Ta": "Тантал",
    "Tb": "Тербий",
    "Tc": "Технеций",
    "Te": "Теллур",
    "Th": "Торий",
    "Ti": "Титан",
    "Tl": "Таллий",
    "Tm": "Тулий",
    "Ts": "Теннессин",
    "U": "Уран",
    "Uue": "Унуненний",
    "V": "Ванадий",
    "W": "Вольфрам",
    "Xe": "Ксенон",
    "Y": "Иттрий",
    "Yb": "Иттербий",
    "Zn": "Цинк",
    "Zr": "Цирконий"
    }
    result = ''
    for i in range(len(string_of_elements)):
        if string_of_elements[i].isupper():
            element = string_of_elements[i]
        elif string_of_elements[i].islower():
            element += string_of_elements[i]
        if i != len(string_of_elements) - 1 and string_of_elements[i + 1].isupper():
            result += periodic_table[element]
    result += periodic_table[element]
    return result


# задача 9
class Student:

    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = f'{name} {surname}'
        self.grades = grades

    def greeting(self):
        return f'Hello, I am a Student {self.__class__}'

    def mean_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_otlichnik(self):
        return ['NO', 'YES'][self.mean_grade() >= 4.5]

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'

    def __str__(self):
        return self.fullname


# задача 10
class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg
