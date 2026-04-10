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

def add_student():
    if len(students) >= MAX_STUDENTS:
        print("\n  [!] Database is full. Cannot add more students.")
        return

    print()
    print_line("─")
    print("  ADD NEW STUDENT")
    print_line("─")


    while True:
        student_id = read_string("  Student ID  : ")
        if find_student(student_id) == -1:
            break
        print(f"  [!] ID '{student_id}' already exists. Use a different ID.")

    first_name  = read_string("  First Name  : ")
    last_name   = read_string("  Last Name   : ")
    course      = read_string("  Course      : ")
    year_level  = read_int   ("  Year Level (1-5): ", 1, 5)
    gwa         = read_float ("  GWA (0-100) : ", 0.0, 100.0)

    students.append({
        "id":         student_id,
        "first_name": first_name,
        "last_name":  last_name,
        "course":     course,
        "year_level": year_level,
        "gwa":        gwa,
    })

    print(f"\n  [✓] Student '{first_name} {last_name}' added successfully!")

def view_all_students():
    print()
    print_line("═")
    print(f"  ALL STUDENTS  ({len(students)}/{MAX_STUDENTS})")
    print_line("═")

    if not students:
        print("  No records found.")
        print_line("═")
        return

    print(f"  {'ID':<12} {'First Name':<20} {'Last Name':<20} {'Course':<15} {'Yr':>3}  {'GWA':>6}")
    print_line("─")

    for s in students:
        print(f"  {s['id']:<12} {s['first_name']:<20} {s['last_name']:<20} "
              f"{s['course']:<15} {s['year_level']:>3}  {s['gwa']:>6.2f}")

    print_line("═")

def search_student():
    print()
    print_line("─")
    print("  SEARCH STUDENT")
    print_line("─")

    student_id = read_string("  Enter Student ID to search: ")
    idx = find_student(student_id)

    if idx == -1:
        print(f"  [!] No student found with ID '{student_id}'.")
        return

    print("\n  [✓] Record found:")
    print_record(students[idx])


def update_student():
    print()
    print_line("─")
    print("  UPDATE STUDENT")
    print_line("─")

    student_id = read_string("  Enter Student ID to update: ")
    idx = find_student(student_id)

    if idx == -1:
        print(f"  [!] No student found with ID '{student_id}'.")
        return

    print("\n  Current Record:")
    print_record(students[idx])
    print("  Enter new details (press Enter to keep current value):\n")

    s = students[idx]

    val = input(f"  First Name   [{s['first_name']}]: ").strip()
    if val:
        s["first_name"] = val

    val = input(f"  Last Name    [{s['last_name']}]: ").strip()
    if val:
        s["last_name"] = val

    val = input(f"  Course       [{s['course']}]: ").strip()
    if val:
        s["course"] = val

    val = input(f"  Year Level   [{s['year_level']}] (1-5, Enter to keep): ").strip()
    if val:
        try:
            yr = int(val)
            if 1 <= yr <= 5:
                s["year_level"] = yr
            else:
                print("  [!] Invalid year level. Kept original.")
        except ValueError:
            print("  [!] Invalid input. Kept original.")

    val = input(f"  GWA          [{s['gwa']:.2f}] (0-100, Enter to keep): ").strip()
    if val:
        try:
            gwa = float(val)
            if 0.0 <= gwa <= 100.0:
                s["gwa"] = gwa
            else:
                print("  [!] Invalid GWA. Kept original.")
        except ValueError:
            print("  [!] Invalid input. Kept original.")

    print("\n  [✓] Record updated.")
    print_record(s)
