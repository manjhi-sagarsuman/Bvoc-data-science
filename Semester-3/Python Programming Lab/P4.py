# Practical 4
name=input("Enter your name:")
salary=float(input("Enter your Monthly Salary:"))
rate=int(input("Enter your performance rating(1-5):"))
if(rate==5):
    bonus_amount= (salary*20)/100
    print("Bonus increased by 20%")
elif(rate==4):
    bonus_amount= (salary*15)/100
    print("Bonus increased by 15%")
elif(rate==3):
    bonus_amount= (salary*10)/100
    print("Bonus increased by 10%")
elif(rate==2):
    bonus_amount= (salary*5)/100
    print("Bonus increased by 5%") 
else:
    bonus_amount=0
    print("No Bonus")    

Total_salary = bonus_amount + salary
print("Bonus Amount: ", bonus_amount)
print("Employee Performance:", rate)
print("Total Salary:", Total_salary)

""" 
# Example 1: Check Positive Number

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")


# Example 2: Check Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Example 3: Student Grade

marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# Example 4: Employee Bonus

salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating (1-5): "))

if rating >= 3:
    if salary >= 30000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.15
else:
    bonus = 0

print("Bonus: Rs.", bonus)
print("Final Salary: Rs.", salary + bonus)


# Example 5: Employee Salary Calculation

salary = float(input("Enter employee salary: "))
experience = int(input("Enter years of experience: "))

if experience >= 10:
    bonus = salary * 0.20
elif experience >= 5:
    bonus = salary * 0.10
elif experience >= 2:
    bonus = salary * 0.05
else:
    bonus = 0

final_salary = salary + bonus

print("Bonus: Rs.", bonus)
print("Final Salary: Rs.", final_salary)


# Example 6: Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
 """