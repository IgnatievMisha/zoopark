class School:
    def __init__(self, name, students):
        self.name=name
        self.students=students #spisok
        self.teachers=[] #1 exercise
        self.classes=[] #2 exercise
    def admit_students(self, student):
        self.students.append(student)
        print(f'{student.name} was admit to school {self.name}') #dopisati
    def expel_student(self, student):
        expelled_student=next(filter(lambda s: s.name==student.name and s.grade==student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(expelled_student)
            print(f'{expelled_student.name} was deleted from {self.name}')
        else:
            print(f'{student.name} was not found {self.name}')
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    def add_class(self, classs):
        self.classes.append(classs)

class Student:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade
    def promote(self):
        self.grade+=1
        print(f'{self.name} was promoted to {self.grade}')
    def demote(self):
        self.grade-=1
        print(f'{self.name} was demote to {self.grade}')
    def __str__(self):
        return f'{self.name} - rank {self.grade}'


'''multiply=lambda x, y: x*y
print(multiply(28,28))
numbers=[1,2,3,4,5,6,7,8,9,10]
filtered_numbers=list(filter(lambda x: x%2==0, numbers))
print(filtered_numbers)'''


Lisa=Student("Alisa", 6)
Masha=Student("Maria", 2)
Andriy=Student("Andriy", 50)
Dima=Student("Dmytro", 23)
Gleb=Student("Glebus", 100)
my_school=School("ItStep", [Lisa, Masha, Andriy, Dima, Gleb])
print("initial students")
for student in my_school.students:
    print(student)

my_school.admit_students(Student("Bogdan", 3))
my_school.expel_student(Student("Glebus", 100))
print("Update")
for student in my_school.students:
    print(student)

#PRAKTICHNA ROBOTA

class Teacher:
    def __init__(self, name, subject, classes):
        self.name=name
        self.subject=subject
        self.classes=classes

class Class:
    def __init__(self, number):
        self.number=number
        self.students=[]
    def add_student(self, student):
        self.students.append(student)