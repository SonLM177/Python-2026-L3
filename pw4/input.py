import math
import curses
from domains import Student, Course

def floor1(x):
    """Round DOWN to 1 decimal: 15.87 -> 15.8"""
    return math.floor(x * 10) / 10

def ask(win, prompt): #curses UI functions
    win.addstr(prompt, curses.color_pair(2))
    curses.echo()
    text = win.getstr().decode().strip()
    curses.noecho()
    return text

def title(win, text):
    win.clear()
    win.addstr(f" {text} \n\n", curses.color_pair(1) | curses.A_BOLD)

def pause(win):
    win.addstr("\nPress any key to continue...", curses.A_DIM)
    win.getch()

def input_students(win): #action functions
    title(win, "ADD STUDENTS")
    n = int(ask(win, "Number of students: "))
    for _ in range(n):
        name = ask(win, "Name: ")
        sid = ask(win, "ID: ")
        dob = ask(win, "DoB: ")
        students.append(Student(sid, name, dob))
        win.addstr("\n")

def input_courses(win):
    title(win, "ADD COURSES")
    n = int(ask(win, "Number of courses: "))
    for _ in range(n):
        name = ask(win, "Course name: ")
        cid = ask(win, "Course ID: ")
        credits = int(ask(win, "Credits: "))
        courses.append(Course(cid, name, credits))
        win.addstr("\n")

def input_marks(win):
    title(win, "INPUT MARKS")
    name = ask(win, "Course name: ")
    course = next((c for c in courses if c.name == name), None)
    if course is None:
        win.addstr("Course not found\n")
    else:
        for s in students:
            s.marks[course.cid] = floor1(float(ask(win, f"Mark for {s.name}: ")))
    pause(win)
