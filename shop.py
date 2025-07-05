class Student:
    def __init__(self, name, shreni, roll):
        self.name = name 
        self.shreni = shreni
        self.roll = roll

    def __repr__(self):
        return (f'{self.name} is admited in class {self.shreni} with id {self.roll}')

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return (f'{self.name} with id {self.id} will conduct {self.subject}')

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def add_student(self, name, shreni, fee):
        if fee < 6000:
            return 'Not emoungh fee'
        else:
            roll = len(self.students)+1
            student = Student(name, shreni, roll)
            self.students.append(student)
            return f'{name} is enrolled with roll {roll} in class {shreni}'
        
    def __repr__(self):
        print()
        print(f'------ Welcome to {self.name} ----------')
        print()
        print('---- Our Teachers ------- ')
        for teacher in self.teachers:
            print(teacher)

        print()
        print('----- Our Student ------ ')
        for student in self.students:
            print(student)
        return f''

        

phitro = School('Phitron')

phitro.add_student('alia', 'Nine', 5400)
phitro.add_student('mousumi', 'seven', 6200)
phitro.add_student('shabnur', 'Ten', 7000)

phitro.add_teacher('Sakib Khan', 'Data Structure')
phitro.add_teacher('Salman Shah', 'Data Science')
phitro.add_teacher('Dipjol', 'Astronimy')


print(phitro)