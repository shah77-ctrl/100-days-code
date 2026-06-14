# Day 13 - Password Strength Checker
# This program checks whether a password is weak, medium, or strong.

password = input("Enter a password to check: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase letters
has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True

if has_uppercase:
    score += 1

# Check lowercase letters
has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True

if has_lowercase:
    score += 1

# Check numbers
has_number = False
for char in password:
    if char.isdigit():
        has_number = True

if has_number:
    score += 1

# Check symbols
has_symbol = False
for char in password:
    if not char.isalnum():
        has_symbol = True

if has_symbol:
    score += 1

print("\nPassword Analysis:")
print(f"Score: {score}/5")

if score <= 2:
    print("Result: Weak Password")
elif score <= 4:
    print("Result: Medium Password")
else:
    print("Result: Strong Password")