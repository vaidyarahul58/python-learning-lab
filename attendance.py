# Storing Keys and values in Dictionary and printing them.
# Printig Keys and values using item functions
students = {"name" : "Priya", "age" : 21, "course" : "Python"}
print(students.keys())
print(students.values())
print(students.items())

# Printing key and its value
print("\n====== Printing key and its value =====")
for key, value in students.items():
    print(f"{key} : {value}")

# Nesting multiple data sets in dictionaries into one dictionary. 
print("\n===== Python Course - Batch 12 : Attendance Sheet ======")
batch_12 = {  
    "S101" : {"name" : "Amit", "marks" : 85},
    "S102" : {"name" : "Priya", "marks" : 92},
    "S103" : {"name" : "Kedar", "marks" : 72}
}     
# Printing student names from data
print(batch_12 ["S101"] ["name"])
print(batch_12 ["S102"] ["name"])
print(batch_12 ["S103"] ["name"])