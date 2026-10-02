import curses
import input as inp   # aliased so it doesn't clash with the built-in input()
import output as out

students = []
courses = []

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

if __name__ == "__main__":
    curses.wrapper(main)