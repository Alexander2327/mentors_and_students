class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        l = 0
        for grades in self.grades.values():
            for grade in grades:
                l += 1
        av_grade = round(sum(map(sum, self.grades.values())) / l, 1)
        return av_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за ДЗ: {self.average_grade()}\nКурсы в ' \
              f'процессе изучения: {", ".join(str(x) for x in self.courses_in_progress)}\nЗавершенные к' \
              f'урсы: {", ".join(str(x) for x in self.finished_courses)} '
        return res

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        else:
            return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        else:
            return self.average_grade() < other.average_grade()

    def rate_lecturer(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and (
                course in self.finished_courses or course in self.courses_in_progress) and course in mentor.courses_attached:
            if 1 <= grade <= 10:
                if course in mentor.grades:
                    mentor.grades[course] += [grade]
                else:
                    mentor.grades[course] = [grade]
            else:
                return 'Неверная оценка!'
        else:
            return 'Невозможно поставить оценку преподавателю!'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        l = 0
        for grades in self.grades.values():
            for grade in grades:
                l += 1
        av_grade = round(sum(map(sum, self.grades.values())) / l, 1)
        return av_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        else:
            return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        else:
            return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grade_course(st_list, course):
    sum_av_grade, l = 0, 0
    for student in st_list:
        if course in student.courses_in_progress:
            sum_av_grade += sum(student.grades[f'{course}'])
            l += len(student.grades[f'{course}'])
    av_grade_course = round(sum_av_grade / l, 2)
    return av_grade_course


def average_grade_course_l(l_list, course):
    sum_av_grade, l = 0, 0
    for lecturer in l_list:
        if course in lecturer.courses_attached:
            sum_av_grade += sum(lecturer.grades[f'{course}'])
            l += len(lecturer.grades[f'{course}'])
    av_grade_course = round(sum_av_grade / l, 2)
    return av_grade_course


best_student = Student('Ella', 'Kharlamova', 'Female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C++']

bed_student = Student('Sanya', 'Danilov', 'Male')
bed_student.courses_in_progress += ['Python']
bed_student.courses_in_progress += ['JavaScript']
bed_student.finished_courses += ['PHP']
bed_student.finished_courses += ['C']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C']
cool_mentor.courses_attached += ['Java']

cool_mentor_2 = Reviewer('Add', 'Tudeski')
cool_mentor_2.courses_attached += ['C++']

bed_mentor = Lecturer('Jimmy', 'Lane')
bed_mentor.courses_attached += ['C++']
bed_mentor.courses_attached += ['Python']

bed_mentor_2 = Lecturer('Jonn', 'Ratalovski')
bed_mentor_2.courses_attached += ['PHP']
bed_mentor_2.courses_attached += ['C']
bed_mentor_2.courses_attached += ['Python']

best_student.rate_lecturer(bed_mentor, 'Python', 8)
best_student.rate_lecturer(bed_mentor, 'Python', 9)
best_student.rate_lecturer(bed_mentor, 'C++', 1)

bed_student.rate_lecturer(bed_mentor, 'C', 3)
bed_student.rate_lecturer(bed_mentor_2, 'PHP', 4)
bed_student.rate_lecturer(bed_mentor_2, 'C', 1)
bed_student.rate_lecturer(bed_mentor_2, 'Python', 10)

cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Java', 2)
cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(bed_student, 'Python', 8)
cool_mentor.rate_hw(bed_student, 'C', 2)
cool_mentor.rate_hw(bed_student, 'C', 9)

cool_mentor_2.rate_hw(best_student, 'C++', 3)
cool_mentor_2.rate_hw(best_student, 'C++', 2)
cool_mentor_2.rate_hw(best_student, 'C++', 6)

# print(best_student)
# print(bed_student)
# print(bed_mentor)
# print(bed_mentor_2)
# print(best_student.grades)
# print(bed_student.grades)
# print(best_student.average_grade())
# print(bed_mentor.grades)
# print(bed_mentor_2.grades)

student_list = [best_student, bed_student]
lecturer_list = [bed_mentor, bed_mentor_2]

# print(average_grade_course(student_list, 'Python'))
# print(average_grade_course_l(lecturer_list, 'Python'))
