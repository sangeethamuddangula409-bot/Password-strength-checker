
import string

common = ["password", "12345678", "qwerty123",
          "admin123", "password123", "123456789"]

def check_password(p):
    score = 0
    tips = []

    if len(p) >= 8:
        score += 20
    else:
        tips.append("Use at least 8 characters")

    if len(p) >= 12:
        score += 10

    if any(c.isupper() for c in p):
        score += 15
    else:
        tips.append("Add uppercase letters")

    if any(c.islower() for c in p):
        score += 15
    else:
        tips.append("Add lowercase letters")

    if any(c.isdigit() for c in p):
        score += 15
    else:
        tips.append("Add numbers")

    if any(c in string.punctuation for c in p):
        score += 15
    else:
        tips.append("Add special characters")

    if p.lower() not in common:
        score += 10
    else:
        score = 0
        tips.append("Avoid common passwords")

    if len(set(p)) <= 3 and len(p) > 3:
        score = min(score, 30)
        tips.append("Avoid excessive character repetition")

    if any(seq in p.lower() for seq in
           ["1234", "abcd", "qwerty"]):
        score = min(score, 40)
        tips.append("Avoid predictable sequences")

    print("\n------ SECURITY REPORT ------")
    print("Password length:", len(p))
    print("Security score:", score, "/ 100")

    if score < 40:
        print("Rating: Weak")
    elif score < 60:
        print("Rating: Medium")
    elif score < 80:
        print("Rating: Strong")
    else:
        print("Rating: Very Strong")

    if tips:
        print("\nSuggestions:")
        for tip in tips:
            print("-", tip)
    else:
        print("Good password complexity!")
    print("-----------------------------")

while True:
    password = input("\nEnter password (or exit): ")

    if password.lower() == "exit":
        print("Thank you for using the checker!")
        break

    if not password:
        print("Password cannot be empty.")
        continue

    check_password(password)

