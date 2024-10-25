
# create a class for student info
class Student:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

        
    # string method to display readable ouput when newly created object is printed
    
    def __str__(self):
        # return f"Student Name:{self.name}, ID:{self.id}, Age:{self.age}, Gender:{self.gender}" this line display all details when obj is printed
        return f"{self.name}({self.gender})"

# create a class for course
class Course:
    def __init__(self, course, branch):
        self.course = course
        self.branch = branch
        
# create a string function
    def __str__(self):
        return f"{self.course} ({self.branch})"   # output will  "B.Tech(AI)", when obj is printed


# create a class for Marks  
class Marks:
    def __init__(self, student, subject, marks, result):
        self.student = student
        self.subject = subject
        self.marks = marks
        self.result = result
              
    def __str__(self):
        return f"{self.student} scored {self.marks} in {self.subject} and Result is {self.result}"

# Create a class Student Management System 
class Stud_Man_Sys:
    def __init__(self):
        self.courses = []    # to manage courses in SMS
        self.students = []   # To manage students in SMS
        self.singlecourse = []  # list of students who registered for one course already

    # add courses in SMS using add_courses method
    def add_courses(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Course {course} was registered and availble for joining new students")
        else:
            print(f"Course {course} already exists")
        
    
    # add students to SMS
    def add_students(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student} was successfully registered")
        else:
            print(f"Student {student} already registered.")
        
    # display courses
    def disply_courses(self):
        print([str(course) for course in self.courses])   # print all courses registered as strings

    
    # Joining courses
    def join_course(self, student, course):
        if student not in self.singlecourse:
            self.singlecourse.append(student)
            print(f"Student {student} joined {course}")   
        else:
            print(f" Student {student} already enrolled for one course.")    
        
    # add marks to student

    def add_student_marks(self, student, marks):
      print(f"Student '{student}' Marks details : {marks}")
        
    # remove students from list
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Student {student} was removed from the list")

        else:
            print(f"Student {student} not registered ")

    def display_students(self):
        print([str(student) for student in self.students])
               
# create instances of classes student, course, SMS, marks    

student1 = Student(1001, "Kumar", 17, "Male")
student2 = Student(1002, "Sravani", 17, "Female")
student3 = Student(1003, "Vishva", 17, "Male")
student4 = Student(1004, "Aadhvitha", 17, "Female")
student5 = Student(1005, "BattulaKumar", 17, "Male")

print(student1) # to check what is displayed when object is printed, __str__ method return value is printed

# create objects for class Course

course1 = Course("B.Tech", "CSc")
course2 = Course("B.Tech", "ECE")
course3 = Course("B.Tech", "AI")
course4 = Course("B.Tech", "ML")
course5 = Course("B.Tech", "Datascience")

print(course1)   # output printed from __str__ method of class Course

# create an instance pf SMS
sms1 = Stud_Man_Sys()

# add new courses to list 
sms1.add_courses(course1)   # Here, course object used not course string directly.
sms1.add_courses(course2)
sms1.add_courses(course3)
sms1.add_courses(course4)
sms1.add_courses(course5)

# add students
sms1.add_students(student1)
sms1.add_students(student2)
sms1.add_students(student3)
sms1.add_students(student4)
sms1.add_students(student5)

# joining courses
sms1.join_course(student1, course1)
sms1.join_course(student2, course2)
sms1.join_course(student3, course3)
sms1.join_course(student4, course4)
sms1.join_course(student5, course5)


# display available courses
sms1.disply_courses()

 # create an instance for class Marks
marks1 = Marks(student1, "mathematics", 89, "Passed")
marks2 = Marks(student2, "Telugu", 80, "Passed")
marks3 = Marks(student3, "Hindi", 82, "Passed")
marks4 = Marks(student4, "English", 75, "Passed")
marks5 = Marks(student5, "Physics", 80, "Passed")

print(marks1)  # output from __str__ method of class Marks


# add Marks to each student object

sms1.add_marks_student(student1, marks1)
sms1.add_marks_student(student2, marks2)
sms1.add_marks_student(student3, marks3)
sms1.add_marks_student(student4, marks4)
sms1.add_marks_student(student5, marks5)

# remove student from the list
sms1.remove_student(student2)

# check  multiple different courses joining. Will display error message. Here one studentallowed to join one course only
sms1.join_course(student1, course2)

# Adding Removed student2 again

sms1.add_students(student2)
sms1.display_student()

## adding again to check error message
sms1.add_students(student2)
sms1.display_student()















    












