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

    def add_grades_lecturer(self, lecturer, course, grade): # Выставление оценок студентами лекторам
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.dict_lecturer:
                lecturer.dict_lecturer[course] += [grade]
            else:
                lecturer.dict_lecturer[course] = [grade]
        else:
            return 'Ошибка'



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.dict_lecturer = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def add_grades_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.dict_student:
                student.dict_student[course] += [grade]
            else:
                student.dict_student[course] = [grade]
        else:
            return 'Ошибка'

student_1= Student('Егор','Бозых','мальчик')
student_1.courses_in_progress.append('Python')

# Выставление оценок проверяющими студентам
reviewer_1 = Reviewer ('Слава','Волков')
reviewer_1.courses_attached.append('Python')

reviewer_1.add_grades_student(student_1, 'Python', 10)
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)

# Студент-1
print(student_1.name)
print(student_1.surname)
print(student_1.gender)
print(student_1.courses_in_progress)
print(student_1.dict_student)

# Проверяющий -1
print(reviewer_1.name)
print(reviewer_1.surname)
print(reviewer_1.courses_attached)

# Выставление оценок студентами лекторам
#Лекторы:
lecturer_1 = Lecturer('Володя','Борисенко')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Python-WEB')

# Студенты:
student_2= Student('Лена','Савина','девочка')
student_2.courses_in_progress.append('Python')
student_3= Student('Татьяна','Лепехина','девочка')
student_3.courses_in_progress.append('Python')
student_4= Student('Женя','Сидоренко','мальчик')
student_4.courses_in_progress.append('Python-WEB')
student_5= Student('Игорь','Спорыхин','мальчик')
student_5.courses_in_progress.append('Python-WEB')

# Оценки лектору №1 :
student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)
student_4.add_grades_lecturer(lecturer_1, 'Python-WEB', 10)
student_5.add_grades_lecturer(lecturer_1, 'Python-WEB', 7)


print(lecturer_1.courses_attached)
print(lecturer_1.dict_lecturer)