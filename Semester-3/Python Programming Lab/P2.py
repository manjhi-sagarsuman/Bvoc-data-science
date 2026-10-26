# Example 1: Basic shopping cart
cart = []

n = int(input("How many items do you want to buy? "))

for i in range(n):
    item = input("Enter item name: ")
    cart.append(item)

print("\nShopping Cart:")
for item in cart:
    print(item)

print("Total items:", len(cart))

# Example 2: String operations
name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))
print("First character:", name[0])
print("Reversed:", name[::-1])

# Example 3: List operations
items = ["Milk", "Bread", "Rice"]

print("Original list:", items)

items.append("Sugar")
print("After adding:", items)

items.remove("Bread")
print("After removing:", items)

print("First item:", items[0])
print("Total items:", len(items))

items.sort()
print("Sorted list:", items)

# Example 4: Shopping cart with prices

items = []
prices = []

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))

    items.append(name)
    prices.append(price)

print("\n--- Shopping Bill ---")

for i in range(len(items)):
    print(items[i], "Rs.", prices[i])

print("Total Amount: Rs.", sum(prices))

# Example 5: Update and delete items
cart = ["Pen", "Book", "Bag"]

print("Original cart:", cart)

cart[0] = "Pencil"
print("Updated cart:", cart)

del cart[1]
print("After deletion:", cart)

cart.insert(1, "Notebook")
print("After insertion:", cart)

#Example 6: Shopping cart menu
cart = []

while True:
    print("\n1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.append(item)

    elif choice == "2":
        print("Cart:", cart)

    elif choice == "3":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found")

    elif choice == "4":
        print("Final cart:", cart)
        break

    else:
        print("Invalid choice")
