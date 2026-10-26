# Example 1: Basic input and output
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
print("Next year age:", age + 1)

# Example 2: Arithmetic operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Cannot divide by zero")
print("Floor Division:", a // b if b != 0 else "Cannot divide by zero")
print("Modulus:", a % b if b != 0 else "Cannot divide by zero")
print("Power:", a ** b)

# Example 3: Data types
name = "Sagar"
age = 19
marks = 85.5
passed = True

print(name, type(name))
print(age, type(age))
print(marks, type(marks))
print(passed, type(passed))

# Example 4: Relational operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)

# Example 5: Logical operators
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Eligible:", age >= 18 and marks >= 40)
print("Any condition true:", age >= 18 or marks >= 40)
print("Not eligible by age:", not (age >= 18))

# Example 6: Assignment operators
a = 10

a += 5
print("After +=:", a)

a -= 3
print("After -=:", a)

a *= 2
print("After *=:", a)

a //= 4
print("After //=:", a)

a %= 3
print("After %=:", a)

a **= 2
print("After **=:", a)

# Example 7: Bitwise operators
a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# Example 8: Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division by zero is not allowed")

# Example 9: Swap two variables
a = input("Enter first value: ")
b = input("Enter second value: ")

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)

# Example 10: Calculate percentage
name = input("Enter student name: ")

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
percentage = total / 300 * 100

print("Student:", name)
print("Total marks:", total)
print("Percentage:", percentage, "%")


