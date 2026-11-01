import string
import getpass

COMMON_PASSWORDS = {
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "monkey",
    "abc123",
    "password1",
    "123456789",
}


def analyze_password(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is a commonly used password."]

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback

def get_strength(score):
    if score <= 2:
        return "WEAK"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "STRONG"

def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = getpass.getpass("\nEnter a password: ")

    score, feedback = analyze_password(password)
    strength = get_strength(score)

    print("\n--- ANALYSIS RESULTS ---")
    print(f"Strength: {strength}")
    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("\nYour password passed all checks!")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()