# Fizz Buzz Game

#Problem Statement: Print numbers from 1 to 50.
#	• If a number is divisible by 3, print "Fizz".
#	• If it is divisible by 5, print "Buzz".
#	• If it is divisible by both 3 and 5, print "FizzBuzz".
#	• Otherwise, just print the number itself.
import random

print("========= Fizz Buzz ========")
print("\nRules : System will generate a random nuber between 1 to 50...")
print("If the number is divisible by 3, its Fizz ")
print("If the number is divisible by 5, its Buzz ")
print("if it is divisible by both 3 and 5, its FizzBuzz")
print("Lets check how much Fizz, Buzz or FizzBuzz you collect in 10 attempts")
print("\nTry your luck.....!")
F = 0
B = 0
FB = 0

for i in range(1, 11):
    input("\nPress any key to continue...")
    n1 = random.randint(1, 50)
    if n1 % 3 == 0 and n1 % 5 == 0:
        print(f"==== FizzBuzz ===={n1}")
        FB += 1
    elif n1 % 3 == 0:
        print(f"==== Fizz ===={n1}")
        F += 1
    elif n1 % 5 == 0:
        print(f"==== Buzz ===={n1}")
        B += 1
    else:
        print(f"\n{n1}... Try your luck again...")

print("\nYour Token limit is Exhausted...")

if F > 0 or B > 0 or FB > 0:
    print(f"Congratulations! So far you have collected {F} Fizz, {B} Buzz and {FB} FizzBuzz")
else:
    print("Sorry! Better luck Next time")    
