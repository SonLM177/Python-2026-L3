import math
import curses
import numpy as np


class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
        self.marks = {}  # course id -> mark

    def gpa(self, courses):
        """Weighted average: sum(mark * credits) / sum(credits)."""
        taken = [c for c in courses if c.cid in self.marks]
        if not taken:
            return 0.0
        marks = np.array([self.marks[c.cid] for c in taken])
        credits = np.array([c.credits for c in taken])
        return float(np.sum(marks * credits) / np.sum(credits))


class Course:
    def __init__(self, cid, name, credits):
        self.cid = cid
        self.name = name
        self.credits = credits


students = []
courses = []


def floor1(x):
    """Round DOWN to 1 decimal: 15.87 -> 15.8"""
    return math.floor(x * 10) / 10


#curses UI functions
def ask(win, prompt):
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


#action functions
def input_students(win):
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


def list_students(win):
    title(win, "STUDENTS")
    for s in students:
        win.addstr(f"{s.sid} | {s.name} | {s.dob}\n")
    pause(win)


def list_courses(win):
    title(win, "COURSES")
    for c in courses:
        win.addstr(f"{c.cid} | {c.name} | {c.credits} credits\n")
    pause(win)


def show_marks(win):
    title(win, "VIEW MARKS")
    name = ask(win, "Course name: ")
    course = next((c for c in courses if c.name == name), None)
    win.addstr("\n")
    if course is None:
        win.addstr("Course not found\n")
    else:
        for s in students:
            if course.cid in s.marks:
                win.addstr(f"{s.name}: {s.marks[course.cid]}\n")
    pause(win)


def show_ranking(win):
    title(win, "GPA RANKING (high -> low)")
    gpas = np.array([s.gpa(courses) for s in students])
    order = np.argsort(gpas)[::-1]  # descending
    for rank, i in enumerate(order, 1):
        win.addstr(f"{rank}. {students[i].name:<20} GPA: {gpas[i]:.2f}\n")
    pause(win)


#main menu
MENU = [
    ("Add students", input_students),
    ("Add courses", input_courses),
    ("Input marks", input_marks),
    ("List students", list_students),
    ("List courses", list_courses),
    ("Show marks of a course", show_marks),
    ("GPA ranking", show_ranking),
]


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)   # title bar
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # prompts
    while True:
        title(stdscr, "STUDENT MARK MANAGEMENT")
        for i, (label, _) in enumerate(MENU, 1):
            stdscr.addstr(f"  {i}. {label}\n")
        stdscr.addstr("  0. Exit\n\n")
        choice = ask(stdscr, "Choose: ")
        if choice == "0":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(MENU):
            try:
                MENU[int(choice) - 1][1](stdscr)
            except ValueError:
                stdscr.addstr("\nInvalid number entered.\n")
                pause(stdscr)


curses.wrapper(main)