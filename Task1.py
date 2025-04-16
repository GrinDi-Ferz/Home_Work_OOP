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


lecturer_1 = Lecturer('Володя','Борисенко')
lecturer_1.courses_attached.append('Dict')

reviewer_1 = Reviewer ('Слава','Волков')
reviewer_1.courses_attached.append('Python')

print(lecturer_1.name)
print(lecturer_1.surname)
print(lecturer_1.courses_attached)

print(reviewer_1.name)
print(reviewer_1.surname)
print(reviewer_1.courses_attached)