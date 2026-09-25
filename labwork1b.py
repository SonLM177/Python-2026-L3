Students=[] # List of tuples cuz we dont need to change anything
Courses=[]  # List of tuples _
Marks={}  # Dictionary


def input_student():
    total_student = int(input("Number of students in class: "))
    for i in range(total_student):
        Students.append((input("Student name: "), int(input("Student ID: ")), input("DoB: ")))  # Appending each tuple
    
def input_course():
    total_course = int(input("Number of courses: "))
    for i in range(total_course):
        Courses.append((input("Course name: "), int(input("Course ID: ")))) # Appending each tuple

def input_mark():
    course = input("Course name to mark students: ")
    for i in Courses:
        if course == i[0]:      # First element of tuple i = name
            Marks[course]={}     # Nested dictionary -> Marks{} contains every course names
            for j in Students:
                mark = int(input(f"{i[0]} mark for {j[0]}: "))  #j[0] = student name. i[0] = course name
                Marks[course][j[0]] = mark   # j[0] (student name) = Key, mark = value
            return
    print("Not found")
    
def list_student():
    print("STUDENT INFO:")
    for i in Students:
        print(f"Student name: {i[0]} - Student ID: {i[1]} - Student DoB: {i[2]}")   #Listing each Student (using tuplrs)

def list_course():
    print("COURSE INFO:")
    for i in Courses:
        print(f"Course name: {i[0]}, Course ID: {i[1]}")    # Listing each Course
        
def student_marks():
    print("VIEWING MARKS:")
    course = input("Course name for viewing marks: ")   
    
    if course in Marks:
        for student_name in Marks[course]: # Loop through each student inside that course
            print(f"Student: {student_name}, Mark: {Marks[course][student_name]}")
    else:
        print("No marks found for this course")
    
input_student()
input_course()
input_mark()

list_student()
list_course()
student_marks()
