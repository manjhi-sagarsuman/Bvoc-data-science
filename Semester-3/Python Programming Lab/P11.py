# Practical 11: GUI Programming Using Tkinter
import tkinter as tk
from tkinter import messagebox

def register_student():
    name = name_entry.get().strip()
    roll_no = roll_entry.get().strip()
    course = course_entry.get().strip()
    age = age_entry.get().strip()

    if not name or not roll_no or not course or not age:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "Please enter a valid age.")
        return

    details = (
        f"Student Name: {name}\n"
        f"Roll Number: {roll_no}\n"
        f"Course: {course}\n"
        f"Age: {age}"
    )

    result_label.config(text=details)
    messagebox.showinfo("Success", "Student registered successfully!")

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    result_label.config(text="")
# Create main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("450x520")
root.resizable(False, False)
# Heading
tk.Label(
    root,
    text="Student Registration Form",
    font=("Arial", 16, "bold")
).pack(pady=15)
# Student Name
tk.Label(root, text="Student Name:").pack()
name_entry = tk.Entry(root, width=35)
name_entry.pack(pady=5)
# Roll Number
tk.Label(root, text="Roll Number:").pack()
roll_entry = tk.Entry(root, width=35)
roll_entry.pack(pady=5)
# Course
tk.Label(root, text="Course:").pack()
course_entry = tk.Entry(root, width=35)
course_entry.pack(pady=5)
# Age
tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root, width=35)
age_entry.pack(pady=5)
# Buttons
tk.Button(
    root,
    text="Register Student",
    command=register_student,
    bg="green",
    fg="white",
    width=20
).pack(pady=10)

tk.Button(
    root,
    text="Clear Fields",
    command=clear_fields,
    width=20
).pack(pady=3)
# Display student details
tk.Label(
    root,
    text="Student Details",
    font=("Arial", 12, "bold")
).pack(pady=8)

result_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 10)
)
result_label.pack(pady=5)
# Run application
root.mainloop()
