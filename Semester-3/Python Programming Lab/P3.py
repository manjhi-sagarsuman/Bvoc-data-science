
'''Practical 3:
Aim: Use Tuple, Set and Dictionary in a singlr Pythion Program
Question:
Write a Pythin Program to store and display Student Details using different collection data types.
Store the students name and Roll Number in a tuple.
Store the students hobbies in a set(Duplicate hobbies should not be stored)
Store the students subject marks in a dictionary. 
Display all the stored information in a readable format.'''

name = input("Enter your Name: ")
roll_no = int(input("Enter your Roll No: "))
student = (name, roll_no)

hobbies = {
    input("Enter Hobby 1: "),
    input("Enter Hobby 2: "),
    input("Enter Hobby 3: ")
}
subject_marks = {
    "Python": int(input("Enter Python Marks: ")),
    "Maths": int(input("Enter Maths Marks: ")),
    "English": int(input("Enter English Marks: "))
}

print("\n----- Student Details -----")
print("Name:", student[0])
print("Roll No:", student[1])
print("\nHobbies:")
print(hobbies)
print("\nSubject Marks:")
print(subject_marks)


""" 
# Example 1: Tuple operations

student = ("Sagar", 101, 85.5)

print("Student Details:", student)
print("Name:", student[0])
print("Roll Number:", student[1])
print("Marks:", student[2])
print("Length:", len(student))
print("First Two Items:", student[:2])


# Example 2: Dictionary operations

student = {
    "name": "Sagar",
    "roll_no": 101,
    "marks": 85
}

print("Student Details:", student)
print("Name:", student["name"])

student["marks"] = 90
print("Updated Marks:", student["marks"])

student["hobby"] = "Gaming"
print("After Adding:", student)

del student["hobby"]
print("After Deletion:", student)

print("All Keys:", student.keys())
print("All Values:", student.values())


# Example 3: Set operations

subjects = {"Python", "DBMS", "Java"}

print("Subjects:", subjects)

subjects.add("Statistics")
print("After Adding:", subjects)

subjects.discard("Java")
print("After Removing:", subjects)

print("Is Python Present:", "Python" in subjects)
print("Total Subjects:", len(subjects))


# Example 4: List operations

subjects = ["Python", "DBMS", "Java"]

print("Subjects:", subjects)

subjects.append("Statistics")
print("After Adding:", subjects)

subjects[0] = "C++"
print("After Updating:", subjects)

subjects.remove("Java")
print("After Deletion:", subjects)

print("First Subject:", subjects[0])

for subject in subjects:
    print(subject)


# Example 5: Student Information

student = {}

student["name"] = input("Enter student name: ")
student["roll_no"] = int(input("Enter roll number: "))
student["subject"] = input("Enter subject: ")
student["hobby"] = input("Enter hobby: ")
student["marks"] = float(input("Enter marks: "))

print("\nStudent Information:")
for key, value in student.items():
    print(key, ":", value)


# Example 6: Set Search

students = {"Sagar", "Rahul", "Amit", "Priya"}

name = input("Enter student name to search: ")

if name in students:
    print("Student Found")
else:
    print("Student Not Found")

print("All Students:", students)
 """