pass="Securenet@123"

if len(pass) < 6:
    strength = "Weak"

elif len(pass) <=10:
    strength = "Medium"
else:
    strength = "Strong"
print(strength)