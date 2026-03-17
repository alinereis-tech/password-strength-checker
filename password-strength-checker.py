import string
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak password"
    elif score == 3 or score == 4:
        return "Medium password"
    else:
        return "Strong password"
    
print("=== Password Strength Checker ===")
password = input("Enter a password to test: ")
result = check_password_strength(password)
print("Password strength:", result)