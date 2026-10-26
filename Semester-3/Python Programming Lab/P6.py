# PRACTICAL 6
import random

def calculate_total(price, quantity):
    return price * quantity
def calculate_discount(amount):
    if amount >= 1000:
        return amount * 0.10
    return 0
def calculate_gst(amount):
    return amount * 0.05

def print_bill(customer, item, subtotal, discount, gst, total, bill_no):
    print("\n--- RESTAURANT BILL ---")
    print("Bill Number:", bill_no)
    print("Customer Name:", customer)
    print("Item:", item)
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("GST: Rs.", round(gst, 2))
    print("Final Total: Rs.", round(total, 2))

customer = input("Enter customer name: ")
item = input("Enter food item: ")
price = float(input("Enter price: Rs. "))
quantity = int(input("Enter quantity: "))

if price >= 0 and quantity > 0:
    subtotal = calculate_total(price, quantity)
    discount = calculate_discount(subtotal)
    gst = calculate_gst(subtotal - discount)
    total = subtotal - discount + gst
    bill_no = random.randint(1000, 9999)

    print_bill(customer, item, subtotal, discount, gst, total, bill_no)
else:
    print("Invalid price or quantity")

""" 
# Example 1: Simple Function

def greet():
    print("Welcome to Restaurant Billing System")

greet()


# Example 2: Function Arguments

def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))


# Example 3: Calculate GST

def calculate_gst(amount):
    return amount * 0.05

bill = float(input("Enter bill amount: "))
gst = calculate_gst(bill)

print("GST:", gst)
print("Total Bill:", bill + gst)


# Example 4: Restaurant Bill

def calculate_bill(price, quantity):
    return price * quantity

def calculate_gst(amount):
    return amount * 0.05

def discount(amount):
    return amount * 0.10 if amount >= 1000 else 0

item = input("Enter food item: ")
price = float(input("Enter price: Rs. "))
quantity = int(input("Enter quantity: "))

subtotal = calculate_bill(price, quantity)
discount_amount = discount(subtotal)
gst = calculate_gst(subtotal - discount_amount)
total = subtotal - discount_amount + gst

print("\n--- Restaurant Bill ---")
print("Item:", item)
print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount_amount)
print("GST (5%): Rs.", gst)
print("Final Bill: Rs.", total)


# Example 5: Factorial Using Recursion

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num >= 0:
    print("Factorial:", factorial(num))
else:
    print("Enter a non-negative number")


# Example 6: Math Module

import math

num = float(input("Enter a number: "))

print("Square Root:", math.sqrt(num) if num >= 0 else "Invalid")
print("Power:", math.pow(num, 2))
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))


# Example 7: Generate Bill Number

import random

bill_no = random.randint(1000, 9999)

print("Restaurant Bill Number:", bill_no)
 """