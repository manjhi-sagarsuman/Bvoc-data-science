# Practical 9: Online Banking System
class InsufficientBalanceError(Exception):
    pass

balance = 10000

try:
    account = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))

    if not account.isdigit() or len(account) != 10:
        raise ValueError("Account number must contain 10 digits")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= amount
    print("Transaction Successful")
    print("Withdrawn: Rs.", amount)
    print("Remaining Balance: Rs.", balance)

except ValueError as e:
    print("Invalid Input:", e)

except InsufficientBalanceError as e:
    print("Transaction Failed:", e)

else:
    print("Transaction completed successfully")

finally:
    print("Thank you for using Online Banking")


""" 
# Example 1: Try-Except

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("Division:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid numbers")


# Example 2: Else and Finally

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input")

else:
    print("Input accepted")

finally:
    print("Program completed")


# Example 3: Multiple Exceptions

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Division by zero is not allowed")


# Example 4: Raise Exception

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible")

except ValueError as e:
    print("Error:", e)


# Example 5: Custom Exception

class InsufficientBalanceError(Exception):
    pass

balance = 5000
amount = float(input("Enter withdrawal amount: "))

try:
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    balance -= amount
    print("Withdrawal successful")
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Invalid amount:", e)

except InsufficientBalanceError as e:
    print("Error:", e)


 """