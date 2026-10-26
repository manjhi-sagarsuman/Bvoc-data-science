# Practical 8: User Registration Validator
import re

name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
password = input("Enter password: ")
pin = input("Enter 6-digit PIN: ")

if not name.strip():
    print("Invalid Name")
elif not re.fullmatch(r'[\w.-]+@[\w.-]+\.\w+', email):
    print("Invalid Email")
elif not re.fullmatch(r'[6-9]\d{9}', phone):
    print("Invalid Phone")
elif not re.fullmatch(r'\d{6}', pin):
    print("Invalid PIN")
elif not re.fullmatch(
    r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$!]).{8,}',
    password
):
    print("Invalid Password")
else:
    print("Registration Successful")


""" 
# Example 1: Pattern Matching

import re

text = "Python is easy to learn"

result = re.search("easy", text)

if result:
    print("Pattern Found")
else:
    print("Pattern Not Found")


# Example 2: Email Validation

import re

email = input("Enter email: ")

pattern = r'^[\w.-]+@[\w.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# Example 3: Phone Validation

import re

phone = input("Enter 10-digit phone number: ")

pattern = r'^[6-9]\d{9}$'

if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")


# Example 4: Password Validation

import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$!]).{8,}$'

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Password must contain uppercase, lowercase, digit, special character (@#$!), and 8 characters")


# Example 5: Find and Replace

import re

text = "I like Java"
result = re.sub("Java", "Python", text)

print("Original:", text)
print("Updated:", result)


# Example 6: String Splitting

import re

text = "Python,Java;C++ HTML"

result = re.split(r'[,;\s]+', text)

print("Split Words:", result)


# Example 7: Extract Numbers

import re

text = "My marks are 85 and 92"

numbers = re.findall(r'\d+', text)

print("Numbers:", numbers)
 """


