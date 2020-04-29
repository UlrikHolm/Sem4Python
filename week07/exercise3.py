import random as rng
import csv
import platform
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        avg_grade = sum(grades)/len(grades)
        return avg_grade
            


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades


class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

def random_student(n):
    male_names=['Knud Bundgaard','Jesper Vinther','Hjalte Smidt','Eigil Lund','Jonathan Kjaer']
    female_names=['Mary Asmussen','Ilse Michaelsen','Anne-Sofie Smidt','Trine Mikkelsen','Yrsa Larsen']

    with open('students.csv', 'w', newline='') as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['NAME','COURSENAME','TEACHER','ECTS','CLASSROOM','GRADE','IMGURL'])

        for i in range(n):

            course1 = Course('Math', '3.114', 'Borge Larsen', rng.randrange(10,30), rng.choice([2,4,7,10,12]))
            course2 = Course('Danish', '3.114', 'Lisa Larsen', rng.randrange(10,30), rng.choice([2,4,7,10,12]))
            course3 = Course('English', '3.113', 'John Johnson', rng.randrange(10,30), rng.choice([2,4,7,10,12]))
            courses = [course1,course2,course3]

            gender=rng.choice(['Male','Female'])
            if gender is 'Male':
                name = rng.choice(male_names)
            else:
                name = rng.choice(female_names)
            ds = DataSheet(rng.sample(courses,1))
            stud = Student(name,gender,ds,'www.image.com')
            output_writer.writerow([stud.name,stud.data_sheet.courses[0].name,
            stud.data_sheet.courses[0].teacher,stud.data_sheet.courses[0].ETCS,
            stud.data_sheet.courses[0].classroom,stud.data_sheet.courses[0].grade,stud.image_url])

def read_students():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            ds = DataSheet([Course(row[1],row[4],row[2],row[3],int(row[5]))])
            stud = Student(row[0],'N/A',ds,row[6])
            students.append(stud)
            students.sort(key=lambda s: s.get_avg_grade(), reverse=True)
       # for stud in students:
            #print(stud.name + ' - ' + stud.image_url + ' - ' + str(stud.get_avg_grade()))
    return students

def student_plotter():
    students = read_students()
    names = []
    avg_grade = []
    for stud in students:
        names.append(stud.name)
        avg_grade.append(stud.get_avg_grade())


    plt.bar(names, avg_grade, width=0.8, align='center')
    plt.ylabel('Avg. Grade')
    plt.xlabel('Name')
    plt.title('Students avg. grade')
    plt.show()

def student_progress():
    students = read_students()

    for stud in students:
        ETCSsum = 0
        for course in stud.data_sheet.courses:
            ETCSsum += int(course.ETCS)
        print(stud.name + ' - ' + str(round((ETCSsum/150)*100, 2))+'%')

student_progress()

#student_plotter()