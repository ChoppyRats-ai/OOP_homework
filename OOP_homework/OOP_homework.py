class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.calculate_avg_grade()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calculate_avg_grade()}'''

    def calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


#-------------------------------------------------------------------
#Глобальные функции
def calculate_avg_hw(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if not grades:
        return 0
    return sum(grades) / len(grades)


def calculate_avg_lecture(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if not grades:
        return 0
    return sum(grades) / len(grades)

#-------------------------------------------------------------------
#Проверки
student1 = Student('Алексей', 'Иванов', 'М')
student1.courses_in_progress = ['Python', 'Java']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Мария', 'Петрова', 'Ж')
student2.courses_in_progress = ['Python', 'JavaScript']
student2.finished_courses = ['Введение в программирование']

lecturer1 = Lecturer('Алексей', 'Сидоров')
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Ольга', 'Иванова')
lecturer2.courses_attached = ['Java']

reviewer1 = Reviewer('Дмитрий', 'Петров')
reviewer1.courses_attached = ['Python']

reviewer2 = Reviewer('Елена', 'Смирнова')
reviewer2.courses_attached = ['Java']

# Выставляем оценки ученикам

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)

reviewer2.rate_hw(student1, 'Java', 7)
reviewer2.rate_hw(student2, 'JavaScript', 8)

# Выставляем оценки лекторам

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 10)

# Выводим информацию
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравниваем студентов и лекторов
print(student1 > student2)
print(lecturer1 < lecturer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(calculate_avg_hw(students, 'Java'))
print(calculate_avg_lecture(lecturers, 'Python'))


