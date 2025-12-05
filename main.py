import random

# SUBJECT LIST
subjects = ["Maths", "Python", "Electronics", "Mechanics", "Chemistry"]

# DATABASES
students = {}        # Stores profile: name, age, dept
student_marks = {}   # Stores marks & CGPA
passwords = {}       # Stores all passwords

# RANDOM DATA FOR 50 STUDENTS
names_pool = [
    "Arjun","Rahul","Riya","Sneha","Karan","Aditi","Nikhil","Meera","Rohit","Kavya",
    "Vikram","Ishita","Pooja","Sanjay","Varun","Devika","Ananya","Manoj","Tarun","Sahana",
    "Ajay","Divya","Abhishek","Harsh","Tanvi","Gaurav","Nisha","Vishal","Ragini","Aman",
    "Yash","Pranav","Chandan","Sameer","Vijay","Tejas","Suresh","Rakesh","Pavan","Darshan",
    "Lakshmi","Preeti","Neha","Shruti","Deepak","Sudeep","Hemant","Rashmi","Kiran","Bhavana"
]

departments = ["CSE", "ECE", "ME", "Civil", "AI/ML"]

def generate_marks():
    return {sub: random.randint(35, 100) for sub in subjects}

def calculate_cgpa(marks):
    return round(sum((m / 10) for m in marks.values()) / len(marks), 2)

# Create 50 random students
for i in range(200):
    name = random.choice(names_pool)
    sid = name.lower()

    age = 18
    dept = random.choice(departments)
    pwd = f"{sid}@123"

    students[sid] = {"Name": name, "Age": age, "Department": dept}
    passwords[sid] = pwd

    marks = generate_marks()
    total = sum(marks.values())
    percent = round((total / 500) * 100, 2)
    cgpa = calculate_cgpa(marks)

    student_marks[sid] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Percentage": percent,
        "CGPA": cgpa
    }

# FUNCTION: CLASS TOPPER
def get_topper():
    topper_id = max(student_marks, key=lambda x: student_marks[x]["Total"])
    t = student_marks[topper_id]

    print("\n================ CLASS TOPPER ================")
    print(f"Name       : {t['Name']}")
    print(f"Total      : {t['Total']} / 500")
    print(f"Percentage : {t['Percentage']}%")
    print(f"CGPA       : {t['CGPA']}")
    print("==============================================\n")

# FUNCTION: SUBJECT AVERAGE
def show_subject_average():
    print("\n============== SUBJECT AVERAGES ==============")
    for sub in subjects:
        avg = sum(student_marks[s]["Marks"][sub] for s in student_marks) / len(student_marks)
        print(f"{sub:<12} : {round(avg, 2)}")
    print("===============================================\n")

# FUNCTION: CHANGE PASSWORD
def change_password():
    print("\n========== CHANGE PASSWORD ==========")
    user_id = input("Enter your Student ID (letters only): ").strip().lower()

    # Auto-create if not exists
    if user_id not in students:
        students[user_id] = {
            "Name": user_id.capitalize(),
            "Age": 18,
            "Department": random.choice(departments)
        }
        passwords[user_id] = f"{user_id}@123"

    old_pwd = input("Enter OLD password: ")

    if old_pwd != passwords.get(user_id):
        print("\n❌ Incorrect old password!\n")
        return

    new_pwd = input("Enter NEW password: ")
    confirm = input("Confirm NEW password: ")

    if new_pwd != confirm:
        print("\n❌ Password mismatch!\n")
        return

    passwords[user_id] = new_pwd
    print("\n✅ Password updated successfully!\n")

# MAIN SYSTEM LOOP
while True:
    print("========= Academic Performance System =========")
    print("1. Login & View Result")
    print("2. Check Class Topper")
    print("3. Subject Average Marks")
    print("4. Change Password")   # Swapped
    print("5. Exit")              # Swapped

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter your Name: ").strip()
        student_id = name.lower()
        password = input("Enter Password: ")

        correct_pwd = passwords.get(student_id, f"{student_id}@123")

        if password != correct_pwd:
            print("\n❌ Incorrect password!\n")
            continue

        print("\n✅ Login Successful!")

        # Auto-add profile if not exists
        if student_id not in students:
            students[student_id] = {
                "Name": name,
                "Age": 18,
                "Department": random.choice(departments)
            }
            passwords[student_id] = f"{student_id}@123"

        # Create marks if new
        if student_id not in student_marks:
            marks = generate_marks()
            total = sum(marks.values())
            percent = round((total / 500) * 100, 2)
            cgpa = calculate_cgpa(marks)

            student_marks[student_id] = {
                "Name": name,
                "Marks": marks,
                "Total": total,
                "Percentage": percent,
                "CGPA": cgpa
            }

        # DISPLAY PROFILE
        print("\n---------------- STUDENT PROFILE ----------------")
        print(f"Name        : {students[student_id]['Name']}")
        print(f"Age         : {students[student_id]['Age']}")
        print(f"Department  : {students[student_id]['Department']}")
        print("-------------------------------------------------\n")

        # DISPLAY RESULT
        print("------------------- RESULT ---------------------")
        for sub, sc in student_marks[student_id]["Marks"].items():
            print(f"{sub:<12}: {sc}")

        print("\nTotal Marks :", student_marks[student_id]["Total"], "/ 500")
        print("Percentage  :", student_marks[student_id]["Percentage"], "%")
        print("CGPA        :", student_marks[student_id]["CGPA"])
        print("-------------------------------------------------\n")

    elif choice == "2":
        get_topper()

    elif choice == "3":
        show_subject_average()

    elif choice == "4":   # Now this is CHANGE PASSWORD
        change_password()

    elif choice == "5":   # Now this is EXIT
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice!\n")