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