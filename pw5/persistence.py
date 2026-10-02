import os
import zipfile
from domains import Student, Course

DATA_FILE = "students.dat"
FILES = ["students.txt", "courses.txt", "marks.txt"]


def compress():
    """Compress all the txt files into students.dat"""
    with zipfile.ZipFile(DATA_FILE, "w", zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            if os.path.exists(name):
                z.write(name)


def load(students, courses):
    """If students.dat exists, decompress it and load the data."""
    if not os.path.exists(DATA_FILE):
        return
    with zipfile.ZipFile(DATA_FILE) as z:
        z.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt") as f:
            for line in f:
                sid, name, dob = line.rstrip("\n").split(",", 2)
                students.append(Student(sid, name, dob))

    if os.path.exists("courses.txt"):
        with open("courses.txt") as f:
            for line in f:
                cid, name, credits = line.rstrip("\n").split(",", 2)
                courses.append(Course(cid, name, int(credits)))

    if os.path.exists("marks.txt"):
        by_id = {s.sid: s for s in students}
        with open("marks.txt") as f:
            for line in f:
                sid, cid, mark = line.rstrip("\n").split(",")
                if sid in by_id:
                    by_id[sid].marks[cid] = float(mark)