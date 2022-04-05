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

