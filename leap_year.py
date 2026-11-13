# Problem Statement: Write a program that asks the user to input a year. The program should check and print whether the year is a leap year or not.

print("======== Leap year Checker =======")
year = int(input("Enter a year : "))
if year % 4 == 0:
    print("Indeed! This is a leap year.")
else:
    print("Ohh! This is not a leap year.")
