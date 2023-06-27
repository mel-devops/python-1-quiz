def youngest_student(students):
    pass # TODO:

    youngest_age = float("-inf")
    youngest_student = None
    for name, age in students.items():
        if age < youngest_age:
            youngest_age = age
            youngest_student = name
    return youngest_student

# students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
# print(youngest_student(students))  # Expected output: "Alice"
