import curses
import numpy as np

def title(win, text):
    win.clear()
    win.addstr(f" {text} \n\n", curses.color_pair(1) | curses.A_BOLD)

def pause(win):
    win.addstr("\nPress any key to continue...", curses.A_DIM)
    win.getch()

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
    order = np.argsort(gpas)[::-1]  #descending
    for rank, i in enumerate(order, 1):
        win.addstr(f"{rank}. {students[i].name:<20} GPA: {gpas[i]:.2f}\n")
    pause(win)