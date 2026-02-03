# Password Strength Checker

![Python](https://img.shields.io/badge/python-3.6+-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Bestbrainof24/Password-Strength-Checker)

## Description
A Python-based command-line tool that evaluates password security by analyzing length, character variety, and common weak patterns, providing immediate feedback and scoring.

## Features
- Multi-factor Scoring System: Evaluates passwords based on three key criteria
- Real-time Feedback: Provides actionable suggestions for improvement
- Color-coded Results: Visual strength indication using colored terminal output
- Weak Pattern Detection: Identifies common vulnerable passwords and patterns
- Detailed Breakdown: Shows individual component scores for better understanding

## Installation
```bash
git clone https://github.com/Bestbrainof24/Password-Strength-Checker.git
cd Password-Strength-Checker
pip install colorama
python checkPassword.py
```

## Usage
Run the script from your terminal:
```bash
python checkPassword.py
```
Then enter passwords when prompted. The program will:
1. Analyze the password
2. Display individual component scores
3. Show overall strength rating
4. Provide improvement feedback
5. Ask if you want to check another password

## Examples
### Example 1: Very Weak Password
```text
Enter a password: abc123
Length score: 1
Character types score: 2
Weak patterns score: -5
Password score: 0
Password strength: Very Weak
=====================Feedback=====================     
Use a mix of uppercase, lowercase, numbers, and symbols
Avoid common patterns and sequences
==================================================
```

### Example 2: Weak Password
```text
Enter a password: Password123
Length score: 3
Character types score: 3
Weak patterns score: -3
Password score: 3
Password strength: Weak
=====================Feedback=====================
Avoid common patterns and sequences
==================================================
```

### Example 3: Medium Password
```text
Enter a password: test@H0me 
Length score: 3
Character types score: 4
Weak patterns score: 0
Password score: 7
Password strength: Medium
=====================Feedback=====================
Good password, but could be better
==================================================
```

### Example 4: Strong Password
```text
Enter a password: MyS3cureP@$$w0rd
Length score: 4
Character types score: 4
Weak patterns score: 0
Password score: 8
Password strength: Strong
=====================Feedback=====================
Great password!
==================================================
```

## How It Works / Scoring System
The checker uses a comprehensive scoring algorithm with three components:
1. **Length Scoring (0-4 points)**
- **0 points:** Less than 6 characters
- **1 point:** 6-8 characters
- **3 points:** 9-12 characters
- **4 points:** More than 12 characters

2. **Character Type Diversity (0-4 points)**
- **1 point:** Including lowercase letters
- **1 point:** Including uppercase letters
- **1 point:** Including numbers
- **1 point:** Including symbols

3. **Weak Pattern Penalties (-3 to 0 points)**
- **-2 points:** Password contains only digits
- **-2 points:** Password contains only lowercase letters
- **-3 points:** Password is in the list of commonly breached passwords

### Final Strength Rating
- **0-2 points:** 🔴 Very Weak (Red)
- **3-5 points:** 🟡 Weak (Yellow)
- **6-7 points:** 🔵 Medium (Blue)
- **8-10 points:** 🟢 Strong (Green)

**Note:** Total score is capped at a minimum of 0 (no negative scores).

## Features in Detail
### Weak Password Detection
The tool checks against a list of commonly breached passwords including:
- "123456", "password", "123456789", "12345678"
- "12345", "1234567", "1234567890", "qwerty"
- "abc123", "password123"

**Note:** This list is not exhaustive and will be expanded in the very near future for better security.

### Feedback System
Based on the analysis, the tool provides specific recommendations:
- **Length issues:** Suggests minimum character requirements
- **Diversity issues:** Recommends using different character types
- **Pattern issues:** Warns about common weak patterns

## Limitations
- The breached password list is small and will be expanded for production use in the very near future.
- Does not check against dictionary words comprehensively.
- No entropy calculation for advanced cryptographic strength analysis.
- Local tool only - no database of known breached passwords [Will Be Upgraded Soon].