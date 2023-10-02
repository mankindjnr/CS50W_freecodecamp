class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


# adding a student to a course
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade() # we are calling the get_grade method of the Student class - consistency in return values
        return value / len(self.students)

# we have created 3 students
student1 = Student("Tim", 19, 95)
student2 = Student("Bill", 19, 75)
student3 = Student("Jill", 19, 65)

# we have created a course
course = Course("Science", 2)

# we have added the students to the course
# the mehtod add_student in the course class takes a student object as an argument
course.add_student(student1)
course.add_student(student2)

# we have printed the name of the students in the course (first student)
# here we are accessing the students attribute of the course object which is an array that is storing the student objects
# from the add_student method
print(course.students[0].name)

# we have printed the average grade of the students in the course
print(course.get_average_grade())

# we have added the third student to the course but we have a max of 2 students - prints false
print(course.add_student(student3))
