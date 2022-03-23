class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        sum_grade = 0
        count = 0
        for grades in self.grades.values():
           for grade in grades:
               sum_grade += grade
               count += 1
        if count == 0:
            av_grade = 0
        else:
            av_grade = round(sum_grade / count, 1)
        return av_grade

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_grade()}\n'
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return result

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            print('Ошибка')

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        else:
            print('Ошибка')


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return result

    def average_grade(self):
        sum_grade = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                sum_grade += grade
                count += 1
        if count == 0:
            av_grade = 0
        else:
            av_grade = round(sum_grade / count, 1)
        return av_grade

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            print('Ошибка')

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        else:
            print('Ошибка')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


student_1 = Student('Павел', 'Савин', 'м')
student_2 = Student('Анастасия', 'Поспелова', 'ж')
lecturer_1 = Lecturer('Светлана', 'Логинова')
lecturer_2 = Lecturer('Елена', 'Пирогова')
reviewer_1 = Reviewer('Александр', 'Вершинин')
reviewer_2 = Reviewer('Леонид', 'Захаровский')

student_1.finished_courses += ['Введение в Python']
student_1.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в Python']
student_2.courses_in_progress += ['Python', 'Git']

lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 4)
student_1.rate_lec(lecturer_2, 'Git', 8)
student_1.rate_lec(lecturer_2, 'Git', 2)
student_2.rate_lec(lecturer_1, 'Python', 7)
student_2.rate_lec(lecturer_1, 'Python', 5)
student_2.rate_lec(lecturer_2, 'Git', 10)

reviewer_1.rate_st(student_1, 'Python', 5)
reviewer_1.rate_st(student_1, 'Python', 10)
reviewer_1.rate_st(student_1, 'Python', 8)
reviewer_1.rate_st(student_2, 'Python', 7)
reviewer_1.rate_st(student_2, 'Python', 8)
reviewer_1.rate_st(student_2, 'Python', 5)

reviewer_2.rate_st(student_1, 'Git', 8)
reviewer_2.rate_st(student_1, 'Git', 8)
reviewer_2.rate_st(student_1, 'Git', 10)
reviewer_2.rate_st(student_2, 'Git', 1)
reviewer_2.rate_st(student_2, 'Git', 8)
reviewer_2.rate_st(student_2, 'Git', 6)

print(student_1 < student_2)
print(student_1 <= student_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 <= lecturer_2)

print()
print('Студенты: ')
print(student_1)
print()
print(student_2)
print('-------------------------------')
print('Лекторы: ')
print(lecturer_1)
print()
print(lecturer_2)
print('-------------------------------')
print('Проверяющие: ')
print(reviewer_1)
print()
print(reviewer_2)
print('-------------------------------')


def average_students_grade(students, course):
    sum_grade = 0
    count = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                for item in value:
                    sum_grade += item
                    count += 1
    res = round(sum_grade/count, 1)
    return res


print(f"Средняя оценка студентов по курсу Python: {average_students_grade([student_1, student_2], 'Python')}")
print(f"Средняя оценка студентов по курсу Git: {average_students_grade([student_1, student_2], 'Git')}")


def average_lecturers_grade(lecturers, course):
    sum_grade = 0
    count = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                for item in value:
                    sum_grade += item
                    count += 1
    res = round(sum_grade/count, 1)
    return res


print(f"Средняя оценка лекторов за лекции по курсу Python: {average_lecturers_grade([lecturer_1, lecturer_2], 'Python')}")
print(f"Средняя оценка лекторов за лекции по курсу Git: {average_lecturers_grade([lecturer_1, lecturer_2], 'Git')}")