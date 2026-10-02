import curses
import input as inp   #aliased so it doesn't clash with the built-in input()
import output as out
import persistence

students = []
courses = []

def add_students(win):
    out.title(win, "ADD STUDENTS")
    inp.input_students(win, students)

def add_courses(win):
    out.title(win, "ADD COURSES")
    inp.input_courses(win, courses)

def add_marks(win):
    out.title(win, "INPUT MARKS")
    inp.input_marks(win, students, courses)
    out.pause(win)

def view_students(win):
    out.title(win, "STUDENTS")
    out.list_students(win, students)
    out.pause(win)

def view_courses(win):
    out.title(win, "COURSES")
    out.list_courses(win, courses)
    out.pause(win)

def view_marks(win):
    out.title(win, "VIEW MARKS")
    name = inp.ask(win, "Course name: ")
    course = next((c for c in courses if c.name == name), None)
    win.addstr("\n")
    if course is None:
        win.addstr("Course not found\n")
    else:
        out.show_marks(win, students, course)
    out.pause(win)

def view_ranking(win):
    out.title(win, "GPA RANKING (high -> low)")
    out.show_ranking(win, students, courses)
    out.pause(win)

#main menu
MENU = [
    ("Add students", add_students),
    ("Add courses", add_courses),
    ("Input marks", add_marks),
    ("List students", view_students),
    ("List courses", view_courses),
    ("Show marks of a course", view_marks),
    ("GPA ranking", view_ranking),
]

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)   #title bar
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  #prompts
    persistence.load(students, courses)          #on start: load saved data
    try:
        while True:
            out.draw_menu(stdscr, MENU)
            choice = inp.ask(stdscr, "Choose: ")
            if choice == "0":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(MENU):
                try:
                    MENU[int(choice) - 1][1](stdscr)
                except ValueError:
                    stdscr.addstr("\nInvalid number entered.\n")
                    out.pause(stdscr)
    finally:
        persistence.compress()                   #before closing: save to students.dat

if __name__ == "__main__":
    curses.wrapper(main)