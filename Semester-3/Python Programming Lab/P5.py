# Practical 5
employees=[
    ("Sagarsuman","Present"),
    ("Rishabh","Absent"),
    ("saiesh","On leave"),
    ("Tulsi","Present"),
    ("Heer","Resigned"),
    ("Ram","Absent")
]

for name, status in employees:
    if status=="Absent":
        continue

    elif status=="On Leave":
        pass
        print(name, "is on Leave")

    elif status=="Resigned":
        print("Processing stopped beczo", name, "Has Resigned")
        break

    else:
        print(name, "is present")

""" 
# Example 1: For Loop

for i in range(1, 6):
    print(i)


# Example 2: While Loop

i = 1

while i <= 5:
    print(i)
    i += 1


# Example 3: ATM Withdrawal

balance = 10000

while True:
    amount = int(input("Enter withdrawal amount (0 to exit): "))

    if amount == 0:
        print("Thank you!")
        break

    if amount < 0:
        print("Invalid amount")
        continue

    if amount > balance:
        print("Insufficient Balance")
        continue

    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)


# Example 4: Break Statement

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Example 5: Continue Statement

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Example 6: Pass Statement

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# Example 7: ATM Menu

balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposit Successful")
        else:
            print("Invalid Amount")

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid Amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Withdrawal Successful")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Choice")
 """