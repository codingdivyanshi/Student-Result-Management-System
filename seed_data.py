"""
seed_data.py
------------
A one-time helper script that fills the database with realistic sample
student records — useful for demos, screenshots, and testing without
typing everything in by hand.

Run it directly from the project root:

    python seed_data.py

It is safe to run only on an empty/fresh database. If student records
already exist, it will ask for confirmation before adding more.
"""

import random
from database.db_manager import DBManager
from utils.grade_calculator import SUBJECTS, calculate_result

# A pool of realistic Indian first and last names to build sample students from
FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan",
    "Krishna", "Ishaan", "Rohan", "Kabir", "Aryan", "Dev", "Yash", "Karan",
    "Ananya", "Diya", "Saanvi", "Aadhya", "Kiara", "Myra", "Pari", "Anika",
    "Ishita", "Riya", "Sneha", "Priya", "Neha", "Pooja", "Simran", "Tanvi",
    "Achat", "Divyanshi", "Rahul", "Amit", "Vikram", "Nikhil", "Suresh", "Rajesh",
]

LAST_NAMES = [
    "Singh", "Sharma", "Verma", "Gupta", "Kumar", "Yadav", "Mishra", "Tiwari",
    "Pandey", "Chauhan", "Rathore", "Rawat", "Joshi", "Dubey", "Shukla", "Agarwal",
    "Patel", "Malhotra", "Kapoor", "Chopra",
]

# Classes typically found in a 10th/12th school setup
CLASSES = ["10th - A", "10th - B", "10th - C", "12th - A", "12th - B", "12th - C"]


def generate_roll_no(index):
    """Generates a simple, realistic roll number like STU101, STU102, etc."""
    return f"STU{100 + index}"


def generate_marks():
    """
    Generates realistic marks for each subject.
    Most students score decently (55-95), but a small number get low marks
    in a subject or two, so the sample data includes some 'Fail' cases too -
    useful to show off the pass/fail logic in a demo.
    """
    marks = []
    for _ in SUBJECTS:
        if random.random() < 0.04:          # ~4% chance of a weak subject
            marks.append(random.randint(15, 39))
        else:
            marks.append(random.randint(55, 100))
    return marks


def seed(total_students=75):
    db = DBManager()

    existing = db.get_all_students()
    if existing:
        print(f"Database already has {len(existing)} student(s).")
        confirm = input("Add more sample students anyway? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cancelled. No changes made.")
            db.close()
            return

    added = 0
    used_names = set()

    for i in range(1, total_students + 1):
        roll_no = generate_roll_no(i)

        # Avoid generating the exact same full name twice, just for realism
        while True:
            name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
            if name not in used_names:
                used_names.add(name)
                break

        student_class = random.choice(CLASSES)
        marks = generate_marks()
        result = calculate_result(marks)

        try:
            db.add_student(roll_no, name, student_class, marks, result)
            added += 1
        except Exception as error:
            print(f"Skipped {roll_no}: {error}")

    print(f"\nDone! Added {added} sample student records to the database.")
    db.close()


if __name__ == "__main__":
    seed(total_students=75)
