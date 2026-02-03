# Length: {weak < 6 = 0, medium 6-8 = 1, upperMedium 9-12 = 3, strong > 12 = 4}
# charTypes: {lowercase = 1, uppercase = 1, numbers = 1, symbols = 1}
# weakPatterns: {onlyInt = -2, onlyLower = -2, breachedPasswords = -3}
# Scale: {0-2 = veryWeak, 3-5 = weak, 6-7 = medium, 8-10 = strong}
def check_length(password: str) -> int:
    if len(password) < 6:
        return 0
    elif len(password) < 9:
        return 1
    elif len(password) < 13:
        return 3
    else:
        return 4

def check_char_types(password: str) -> int:
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1
    return score

def check_weak_patterns(password: str) -> int:
    score = 0
    if password.isdigit():
        score -= 2
    if password.islower():
        score -= 2
    if password in ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "password123"]:
        score -= 3
    return score

def check_password(password: str) -> int:
    length_score = check_length(password)
    char_types_score = check_char_types(password)
    weak_patterns_score = check_weak_patterns(password)
    total_score = length_score + char_types_score + weak_patterns_score
    return 0 if total_score < 0 else total_score

def get_message(score: int) -> str:
    if score < 3:
        return "Very Weak"
    elif score < 6:
        return "Weak"
    elif score < 8:
        return "Medium"
    else:
        return "Strong"

def main() -> None:
    password = input("Enter a password: ")
    score = check_password(password)
    message = get_message(score)
    print(f"Password score: {score}")
    print(f"Password strength: {message}")

if __name__ == "__main__":
    main()