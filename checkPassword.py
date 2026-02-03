# Length: {weak < 6 = 0, medium 6-8 = 1, upperMedium 9-12 = 3, strong > 12 = 4}
# charTypes: {lowercase = 1, uppercase = 1, numbers = 1, symbols = 1}
# weakPatterns: {onlyInt = -2, onlyLower = -2, breachedPasswords = -3}
# Scale: {0-2 = veryWeak, 3-5 = weak, 6-7 = medium, 8-10 = strong}
from colorama import Fore

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
    if password.lower().strip() in ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "password123"]:
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
        return Fore.RED + "Very Weak" + Fore.RESET
    elif score < 6:
        return Fore.YELLOW + "Weak" + Fore.RESET
    elif score < 8:
        return Fore.BLUE + "Medium" + Fore.RESET
    else:
        return Fore.GREEN + "Strong" + Fore.RESET

def get_feedback(length: int, char_types: int, weak_patterns: int, score: int) -> str:
    feedback = []
    if length < 6:
        feedback.append("Make it at least 6 characters long")
    if char_types < 3:
        feedback.append("Use a mix of uppercase, lowercase, numbers, and symbols")
    if weak_patterns < 0:
        feedback.append("Avoid common patterns and sequences")
    if get_message(score) == Fore.GREEN + "Strong" + Fore.RESET:
        feedback.append("Great password!")
    elif get_message(score) == Fore.BLUE + "Medium" + Fore.RESET:
        feedback.append("Good password, but could be better")
    else:
        feedback.append("Consider improving your password")
    return "\n".join(feedback)

def main() -> None:
    again: bool = True
    while again:
        try:
            password: str = input("Enter a password: ")
            if password.strip() == "":
                print("Password cannot be empty")
                continue
            score = check_password(password)
            message = get_message(score)
            print(f"Length score: {check_length(password)}")
            print(f"Character types score: {check_char_types(password)}")
            print(f"Weak patterns score: {check_weak_patterns(password)}")
            print(f"Password score: {score}")
            print(f"Password strength: {message}")
            print(f"{'Feedback':=^50}")
            print(get_feedback(len(password), check_char_types(password), check_weak_patterns(password), score))
            print("=" * 50)
            again = input("Do you want to check another password? (y/n): ")
            if again.lower().strip() not in ["y", "yes"]:
                again = False
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    main()