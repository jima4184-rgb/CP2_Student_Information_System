students = []  
MAX_STUDENTS = 100


def print_line(char="─", length=52):
    print(char * length)


def read_string(prompt):
    """Read a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please try again.")


def read_int(prompt, lo, hi):
    """Read a validated integer within [lo, hi]."""
    while True:
        try:
            value = int(input(prompt).strip())
            if lo <= value <= hi:
                return value
            print(f"  [!] Enter a number between {lo} and {hi}.")
        except ValueError:
            print(f"  [!] Invalid input. Enter a whole number.")


def read_float(prompt, lo, hi):
    """Read a validated float within [lo, hi]."""
    while True:
        try:
            value = float(input(prompt).strip())
            if lo <= value <= hi:
                return value
            print(f"  [!] Enter a value between {lo} and {hi}.")
        except ValueError:
            print(f"  [!] Invalid input. Enter a number (e.g. 88.5).")


def find_student(student_id):
    """Return index of student by ID, or -1 if not found."""
    for i, s in enumerate(students):
        if s["id"] == student_id:
            return i
    return -1


def print_record(student):
    """Print a single student record."""
    print_line()
    print(f"  Student ID   : {student['id']}")
    print(f"  Full Name    : {student['first_name']} {student['last_name']}")
    print(f"  Course       : {student['course']}")
    print(f"  Year Level   : {student['year_level']}")
    print(f"  GWA          : {student['gwa']:.2f}")
    print_line()
