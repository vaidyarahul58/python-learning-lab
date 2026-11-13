# A Computer assessories store having inventory list checking stock EOD.
# Update the inventory list start of business day.

laptop = ["Dell Laptop", "HP Laptop", "Lenovo Laptop",]
mouse = ["Logitech Wired Mouse", "HP Wired Mouse", "Logitech Wireless Mouse", "HP Wireless Mouse"]
keyboard = ["Logitech Wired Keyboard", "HP Wired Keyboard", "Logitech Wireless Keyboard", "HP Wireless Keyboard"]
monitor = ["Dell Monitor", "HP Monitor", "Lenovo Monitor"]

# Printing the inventory Report.
print("\nInventory Report : 01 October 2026")
print("====================================")
print("Laptops:")
for item in laptop:
    print(f" - {item}")

print("\nMice:")
for item in mouse:
    print(f" - {item}")

print("\nKeyboards:")
for item in keyboard:
    print(f" - {item}")

print("\nMonitors:")
for item in monitor:
    print(f" - {item}") 

# Store added dealership of Asus and Acer products.
laptop.extend(["Asus Laptop", "Acer Laptop"]) # add another list to the existing list.
monitor.append("Asus Monitor") # add a single item to the existing list in the end.
keyboard.insert(2, "Acer Wired Keyboard") # add a single item to the existing list in the specific index.

# Store run out of HP Wireless mouse.
mouse.remove("HP Wireless Mouse") # remove a single item from the existing list.

# Printing the inventory Report.
print("\nInventory Report : 02 October 2026")
print("====================================")
print("Laptops:")
for item in laptop:
    print(f" - {item}")

print("\nMice:")
for item in mouse:
    print(f" - {item}")

print("\nKeyboards:")
for item in keyboard:
    print(f" - {item}")

print("\nMonitors:")
for item in monitor:
    print(f" - {item}")

# Asus Laptops found damaged, hence removed from the inventory list.
del laptop[3] # remove a specific item from the existing list using index.

# Printing the inventory Report.
print("\nInventory Report : 03 October 2026")
print("====================================")
print("Laptops:")
for item in laptop:
    print(f" - {item}")

print("\nMice:")
for item in mouse:
    print(f" - {item}")

print("\nKeyboards:")
for item in keyboard:
    print(f" - {item}")

print("\nMonitors:")
for item in monitor:
    print(f" - {item}")