# Python Programming Lab

This directory contains the practical programs and supporting documents for the
**Python Programming Lab** in Semester 3 of the B.Voc. Data Science program.
The exercises progress from Python fundamentals to file handling, GUI
programming, and Excel-based record management.

## Learning outcomes

After completing these practicals, students should be able to:

- Read input, display output, and use Python operators and built-in data types.
- Work with strings, lists, tuples, sets, and dictionaries.
- Apply conditional statements, loops, and loop-control statements.
- Define functions and use classes and objects to model real-world problems.
- Validate user input with regular expressions and handle exceptions safely.
- Read, write, rename, and process text files.
- Build a basic desktop form using Tkinter.
- Perform CRUD (Create, Read, Update, and Delete) operations in an Excel
  workbook using `openpyxl`.

## Practical programs

| Program | Topic | Main concepts |
| --- | --- | --- |
| [P1.py](./P1.py) | Python basics and operators | Input/output, data types, arithmetic, relational, logical, assignment, and bitwise operators |
| [P2.py](./P2.py) | Lists and strings | String operations, list modification, shopping cart, and bill calculation |
| [P3.py](./P3.py) | Collections | Tuples, sets, dictionaries, and student information |
| [P4.py](./P4.py) | Conditional statements | `if`, `elif`, `else`, employee performance, and salary bonus calculation |
| [P5.py](./P5.py) | Loops and control flow | `for`, `while`, `break`, `continue`, and `pass` |
| [P6.py](./P6.py) | Functions and modules | Reusable functions, restaurant billing, discount, GST, and random bill numbers |
| [P7.py](./P7.py) | Object-oriented programming | Classes, objects, constructors, methods, and vehicle rental calculation |
| [P8.py](./P8.py) | Regular expressions | Name, email, phone, PIN, and password validation |
| [P9.py](./P9.py) | Exception handling | Validation, `try`/`except`/`else`/`finally`, and a custom exception |
| [P10.py](./P10.py) | File handling | Creating, renaming, reading, and summarizing expense records |
| [P11.py](./P11.py) | GUI programming | Tkinter student registration form, validation, and form reset |
| [P12.py](./P12.py) | Excel record management | Student CRUD operations with `openpyxl` |

## Supporting material

The [`Lab_Doc`](./Lab_Doc) directory contains the practical documentation in
both DOCX and PDF formats:

- `py1` through `py12`: documentation corresponding to the twelve programs.
- [`sample format for practical.docx`](./Lab_Doc/sample%20format%20for%20practical.docx):
  a sample format for preparing practical work.

The [`student_registration.xlsx`](./student_registration.xlsx) workbook is
included as a supporting spreadsheet file. `P12.py` creates and maintains its
own `student_details.xlsx` workbook in the current working directory.

## Requirements

- Python 3.8 or later.
- Tkinter, which is included with most standard Python installations and is
  required by `P11.py`.
- `openpyxl` for `P12.py`.

Install the Excel dependency with:

```bash
python -m pip install openpyxl
```

## Running a practical

Open a terminal in this directory and run the required program:

```bash
python P1.py
```

Replace `P1.py` with `P2.py` through `P12.py` as needed. Most programs accept
input interactively. `P10.py` creates and renames expense files in the current
working directory, while `P11.py` opens a desktop window and `P12.py` stores
student records in `student_details.xlsx`.

> **Note:** Run the programs in a separate practice directory if you do not
> want generated files such as `expenses.txt`, `my_expenses.txt`, or
> `student_details.xlsx` in the repository folder.
