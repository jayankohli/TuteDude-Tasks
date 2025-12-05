students = {
    "Ram": 85,
    "Sham": 78,
    "Jay": 92
}

name = input("Enter the student's name: ")

if name in students:
    print(name + "'s marks:", students[name])
else:
    print("Student not found.")
