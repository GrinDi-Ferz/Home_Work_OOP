class Mentor:
    mentor_list = []
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Добавленные курсы
        self.dict_lecturer = {} # Оценками лекторам от студентов
        self.average_grade = 0      # Средняя оценка за лекции
        self.mentor_list.append(self)  # Добавим в список преподователей вновь созданный экземпляр

class Student:
    student_list = []
    def __init__(self,name,surname,gender,):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.student_list.append(self) # Добавим в список студентов вновь созданный экземпляр
        self.courses_in_progress = []  # Изучаемые на данный момент курсы
        self.dict_student = {}  # Словарь с оценками студентов от проверяющих
        self.average_grade = 0 # Средняя оценка за ДЗ


    def add_courses (self,course_name): # Добавления пройденных курсов
        self.finished_courses.append(course_name)

    def average_grade_student(self): # Вычисления средней оценки за ДЗ
        grade_list=[]
        for gra in self.dict_student.values():
            grade_list.extend(gra)
        sum_=sum(grade_list)
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    def add_grades_lecturer(self, lecturer, course, grades): # Выставление оценок студентами лекторам
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.dict_lecturer:
                lecturer.dict_lecturer[course] += [grades]
            else:
                lecturer.dict_lecturer[course] = [grades]
        else:
            print('Ошибка')

    def __str__(self): # Волшебный метод __str__  для Студентов
        data = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
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
    def average_grade_lectures(self): # Вычисление средней оценки за лекции
        grade_list=[]
        for gra in self.dict_lecturer.values():
            grade_list.extend(gra)
        sum_=sum(grade_list)
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    def __lt__(self, other): # Сравнение средних оценок лекторов
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade


    def __str__(self): # Волшебный метод __str__ для Лекторов
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grades_student(self, student, course, grades): # Выставка оценок проверяющими студентам
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.dict_student:
                student.dict_student[course] += [grades]
            else:
                student.dict_student[course] = [grades]
        else:
            print('Ошибка')

    def __str__(self): # Волшебный метод __str__ для Проверяющих
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Проверка метода __str__ для проверяющих:
reviewer_1 = Reviewer ('Слава','Волков')
print(reviewer_1)

# Лекторы:
lecturer_1 = Lecturer('Володя','Борисенко')
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
student_4 = Student('Женя','Сидоренко','мальчик')
student_4.courses_in_progress.append('Python Web')
student_5 = Student('Игорь','Спорыхин','мальчик')
student_5.courses_in_progress.append('Python Web')

# Оценки лектору №1
student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)

# Оценки лектору №2
student_1.add_grades_lecturer(lecturer_2, 'Python', 9)
student_2.add_grades_lecturer(lecturer_2, 'Python', 8)
student_3.add_grades_lecturer(lecturer_2, 'Python', 8)

# Оценки обоих лекторов:
print(lecturer_1.dict_lecturer) # {'Python': [9, 9, 10]}
print(lecturer_2.dict_lecturer) # {'Python': [9, 8, 8]}

# Средняя оценка лектора №1
print(lecturer_1.average_grade_lectures())

# Метода __str__ для лектора:
print(lecturer_1)

# Оценки проверяющим студентами
reviewer_1 = Reviewer ('Слава','Волков')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('Python Web')

reviewer_1.add_grades_student(student_1, 'Python', 10)
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)
print(f'Оценки для student_1 - {student_1.dict_student}')

reviewer_1.add_grades_student(student_2, 'Python', 8)
reviewer_1.add_grades_student(student_2, 'Python', 9)
reviewer_1.add_grades_student(student_2, 'Python', 9)
print(f'Оценки для student_2 - {student_2.dict_student}')

reviewer_1.add_grades_student(student_3, 'Python', 8)
reviewer_1.add_grades_student(student_3, 'Python', 9)
reviewer_1.add_grades_student(student_3, 'Python', 8)
print(f'Оценки для student_3 - {student_3.dict_student}')

reviewer_1.add_grades_student(student_4, 'Python Web', 8)
reviewer_1.add_grades_student(student_4, 'Python Web', 7)
reviewer_1.add_grades_student(student_4, 'Python Web', 8)
print(f'Оценки для student_4 - {student_4.dict_student}')

reviewer_1.add_grades_student(student_5, 'Python Web', 6)
reviewer_1.add_grades_student(student_5, 'Python Web', 8)
reviewer_1.add_grades_student(student_5, 'Python Web', 6)
print(f'Оценки для student_5 - {student_5.dict_student}')

# Средняя оценка student_1:
print(student_1.average_grade_student())

# Добавим курс в список текущих курсов студентов
student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)

# Добавим курс в список оконченных курсов:
student_1.finished_courses.append('Введение в программирование')

# Метода __str__ для студента:
print(student_1)

# Словари с оценками у лекторов:
print (lecturer_1.dict_lecturer)
print (lecturer_2.dict_lecturer)

# Средние оценки лекторов №1 и №2:
lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()
print(lecturer_1.average_grade,lecturer_2.average_grade)

# Сравнение лекторов по средним оценкам за лекции
print(lecturer_1 < lecturer_2)

# Средние оценки студентов 1 и 2:
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade)

# Сравним студентов по средней оценке по ДЗ:
print(student_1 > student_2)

# Средняя оценка за домашние задания по всем студентам
def get_average_grade_student_course (other_list,course):
    all_grades_list_course = []
    for student in other_list:
        for key, vul in student.dict_student.items():
            if key == course:
                all_grades_list_course.extend(vul)
    sum_ = sum(all_grades_list_course)
    average_grade_student = round(sum_ / len(all_grades_list_course), 2)
    return average_grade_student

# Средняя оценка за ДЗ студентов для 2-х курсов :
print(get_average_grade_student_course (Student.student_list,"Python"))
print(get_average_grade_student_course (Student.student_list,'Python Web'))


# Формирование списка курсов лекторов
def get_lecturer_course(other_list):
    lecturer_course_all = []
    for mentor in other_list:
        if len(mentor.dict_lecturer) > 0:
            lecturer_course_all.extend(mentor.courses_attached)
    lecturer_course_list = list(set(lecturer_course_all))
    return lecturer_course_list

# Проверка
print(get_lecturer_course(Mentor.mentor_list))

# Средняя оценка за лекции всех лекторов c проверкой
def get_average_grade_mentor_course (other_list,course):
    lecturer_course_list = get_lecturer_course(other_list)
    if course not in lecturer_course_list :
        print('Ошибка.Такого курса нет в списке курсов лекторов')
        return
    all_grades_lecturer_course = []
    for lecturer in other_list:
        if len(lecturer.dict_lecturer) > 0:
            for key, vul in lecturer.dict_lecturer.items():
                if key == course:
                    all_grades_lecturer_course.extend(vul)
    sum_ = sum(all_grades_lecturer_course)
    average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
    return average_grade_lecturer

# Средняя оценка за лекции всех лекторов
print(get_average_grade_mentor_course(Mentor.mentor_list,'Python'))
# Введение курса не правильно:
print(get_average_grade_mentor_course(Mentor.mentor_list,'ython'))