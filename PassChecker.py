#imports Python’s regular expression module, which lets us search for patterns inside text
import re

print("----------PASSWORD STRENGTH CHECKER----------")
password = input("Enter Password: ")

strength =0
print("FEEDBACK:")

#checks for the length of the pasword
if len(password) > 8:
    strength += 1
else:
    print("-Password must be at least 8 characters long.")

#checks if upper and lowercase letters A-Z is present in the password
if re.search(r"[A-Z]", password) and (r"[a-z]", password):
    strength += 1
else:
    print("-Add both UPPERCASE and LOWERCASE letters.")

#checks if special characters is present in the password
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
else:
    print("-Add special characters (!, @, #, etc).")

#checks if any digit is present in the password
if re.search(r"[0-9]", password):
    strength += 1
else:
    print("-Add at least one number.")

#checks the strength of the passwordd
if strength == 4:
    rating = "Strong"
elif strength == 3:
    rating = "Moderate"
else:
    rating = "Weak"
print("Password Strength: ", rating)