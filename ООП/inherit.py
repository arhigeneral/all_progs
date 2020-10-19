class SchoolMember:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary, vagina):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        self.vagina = vagina
        print('(Создан Teacher: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}" Писечка "{1}"'.format(self.salary,self.vagina))


class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks, dick):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        self.dick = dick
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}" Член: "{1}"'.format(self.marks,self.dick))

t = Teacher('Mrs. Nikolaeva', 17, 100000, 'Прекрасная')
s = Student('Popov', 19, 3, 'Гигантский')

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента
