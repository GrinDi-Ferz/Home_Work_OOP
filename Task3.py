class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.dict_student = {}
        self.average_grade = 0

    def add_grades_lecturer(self, lecturer, course, grade): # Выставление оценок студентами лекторам
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.dict_lecturer:
                lecturer.dict_lecturer[course] += [grade]
            else:
                lecturer.dict_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_student(self):    # Вычисления средней оценки за ДЗ
        grade_list=[]
        for gra in self.dict_student.values():
            grade_list.extend(gra)
        sum_grade=sum(grade_list)
        self.average_grade = round(sum_grade/len(grade_list),2)
        return self.average_grade

    def __str__(self):      # Волшебный метод __str__  для Студентов
        data = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за ' \
        f'домашние задания {self.average_grade_student()} \n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return data

    def __lt__(self, other): # Сравнение средних оценок студентов
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.dict_lecturer = {}

    def average_grade_lecturer(self):    # Вычисление средней оценки за лекции
        grade_list=[]
        for gra in self.dict_lecturer.values():
            grade_list.extend(gra)
        sum_grade=sum(grade_list)
        self.average_grade = round(sum_grade/len(grade_list),2)
        return self.average_grade

    def __lt__(self, other): #сравнение средних оценок Лектора
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade

    def __str__(self): # Волшебный метод __str__ для Лекторов
        data = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade_lecturer()}'
        return data

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grades_student(self, student, course, grade): # Выставка оценок проверяющими студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.dict_student:
                student.dict_student[course] += [grade]
            else:
                student.dict_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self): # Волшебный метод __str__ для Проверяющих
        data = f'Имя: {self.name} \n Фамилия: {self.surname}'
        return data

# Лекторы:
(lecturer_1) = Lecturer('Володя','Борисенко')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Наталья','Кириллова')
lecturer_2.courses_attached.append('Python')

# Студенты:
student_1= Student('Егор','Борзых','мальчик')
student_1.courses_in_progress.append('Python')
student_2= Student('Лена','Савина','девочка')
student_2.courses_in_progress.append('Python')
student_3= Student('Татьяна','Лепехина','девочка')
student_3.courses_in_progress.append('Python')

# Оценки Лектору №1
student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)

# Оценки Лектору №2
student_1.add_grades_lecturer(lecturer_2, 'Python', 9)
student_2.add_grades_lecturer(lecturer_2, 'Python', 8)
student_3.add_grades_lecturer(lecturer_2, 'Python', 8)

# Оценки обоих лекторов:
print(lecturer_1.dict_lecturer)
print(lecturer_2.dict_lecturer)

# Вычисление средней оценки лектора №1
print(lecturer_1.average_grade_lecturer())

# Метод __str__ для лекторов:
print(lecturer_1)

# Проверяющие
reviewer_1 = Reviewer ('Слава','Волков')
reviewer_1.courses_attached.append('Python')

# Оценки проверяющими студентам
reviewer_1.add_grades_student(student_1, 'Python', 10)
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)
print(f'Оценки для student_1 - {student_1.dict_student}')

reviewer_1.add_grades_student(student_2, 'Python', 8)
reviewer_1.add_grades_student(student_2, 'Python', 9)
reviewer_1.add_grades_student(student_2, 'Python', 9)
print(f'Оценки для student_2 - {student_2.dict_student}')

# Средняя оценка для student_1:
print(student_1.average_grade_student())

# Добавление курса в список текущих курсов
student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)

# Добавление курса в список оконченных курсов:
student_1.finished_courses.append('Введение в программирование')

# Метода __str__ для студентов:
print(student_1)


# Сравнение между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

# Проверим словари с оценками у лекторов:
print (lecturer_1.dict_lecturer)
print (lecturer_2.dict_lecturer)

# Средние оценки лекторов №1 и №2 :
lecturer_1.average_grade = lecturer_1.average_grade_lecturer()
lecturer_2.average_grade = lecturer_2.average_grade_lecturer()
print(lecturer_1.average_grade,lecturer_2.average_grade)

# Сравнение лекторов по средним оценкам за лекции
print(lecturer_1 < lecturer_2) # False

# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade)

# Сравним студентов по средней оценке по ДЗ:
print(student_1 > student_2) # True