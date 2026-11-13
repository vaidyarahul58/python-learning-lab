# Program for input student details and calculate total marks and percentage.  
# Display Grade.

st_nm = input("Enter Student Name: ")
st_roll = int(input("Enter Student Roll Number: "))
st_maths = int(input("Enter Mathematics Marks: "))
st_science = int(input("Enter Science Marks: "))
st_english = int(input("Enter English Marks: "))

# Validation for marks should be between 0 and 100

if not st_maths in range(1, 101) or not st_science in range(1, 101) or not st_english in range(1, 101):
    print("Invalid Input : Marks should be between 1 and 100.")
    exit()

# Calculate total marks and percentage

total_marks = st_maths + st_science + st_english
percentage = (total_marks / 300) * 100
if st_maths < 35 or st_science < 35 or st_english < 35:
    result = "Fail"
elif percentage >= 90:
    result = "Grade A"
elif percentage >= 75:
    result = "Grade B"
elif percentage >= 60:
    result = "Grade C"
else:
    result = "PASS"

# Printing the student details, total marks, percentage and result

print("=================OUTPUT=================")
print(f"Student Name: {st_nm}")
print(f"Roll Number: {st_roll}")
print(f"Mathematics Marks: {st_maths}")
print(f"Science Marks: {st_science}")
print(f"English Marks: {st_english}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%     Result : {result}")
print("========================================")