# Practical 10: Expense Records Using File Handling
import os

print("--- Sagarsuman Manjhi ---")

# Create and write expense records
with open("expenses.txt", "w") as file:
    file.write("Food,150\n")
    file.write("Travel,80\n")
    file.write("Stationary,100\n")
# Check if the file exists
if os.path.exists("expenses.txt"):
    print("File exists")
else:
    print("File does not exist")
# Rename the file safely
try:
    if os.path.exists("my_expenses.txt"):
        os.remove("my_expenses.txt")

    os.rename("expenses.txt", "my_expenses.txt")
    print("File renamed successfully")
    # Get file size
    size = os.path.getsize("my_expenses.txt")
    print("File Size:", size, "bytes")
    # Read and calculate expense records
    total = 0
    count = 0

    print("\nExpense Records")
    with open("my_expenses.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            item = data[0]
            amount = float(data[1])

            print(item, "-", amount)

            total += amount
            count += 1

    print("\nTotal Expenditure:", total)
    print("Number of Records:", count)

except FileNotFoundError:
    print("File does not exist")

except OSError as e:
    print("File operation failed:", e)
