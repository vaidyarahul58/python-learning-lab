# The Multi-Criteria Password Strength Validator.
# Problem Statement: Create a basic password validator. Ask the user to input a password string. Check if the password meets the following criteria:
# 	• It must be at least 8 characters long.
#	• It must contain at least one digit (use a loop to check each character with .isdigit()).
#	• It must contain at least one special character like @, #, or $.
# Print a message saying whether the password is "Strong" or "Weak".

pw = input("Enter your password : ")
if len(pw) >= 8 and any(ch.isdigit() for ch in pw) and "@" in pw or "#" in pw or "$" in pw:
    print("\nYou have a Strong Password.")
else:
    print("\nYour password is week. Try again...!")
    print("     It must be at least 8 characters long.")
    print("     It must contain at least one digit.")
    print("     It must contain at least one special character.")
