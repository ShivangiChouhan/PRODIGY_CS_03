import re
from typing import Tuple
import time

def check_password_strength(password: str) -> Tuple[str, list, float]:
    """Analyze password strength based on various criteria."""
    feedback = []
    score = 0
    
    # Check length
    length = len(password)
    if length < 8:
        feedback.append("[-] Too short - add more characters")
    elif length < 12:
        feedback.append("[!] Good length, but could be longer")
        score += 20
    else:
        feedback.append("[+] Excellent length")
        score += 40
        
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        feedback.append("[+] Has uppercase letters")
        score += 10
    else:
        feedback.append("[-] Add some uppercase letters")
        
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        feedback.append("[+] Has lowercase letters")
        score += 10
    else:
        feedback.append("[-] Add some lowercase letters")
        
    # Check for numbers
    if re.search(r'\d', password):
        feedback.append("[+] Has numbers")
        score += 10
    else:
        feedback.append("[-] Add some numbers")
        
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("[+] Has special characters")
        score += 10
    else:
        feedback.append("[-] Add special characters (!@#$%^&*)")
        
    # Check for common patterns
    common_patterns = ['12345', 'qwerty', 'password', 'admin', 'abc123']
    for pattern in common_patterns:
        if pattern in password.lower():
            feedback.append(f"[!] Contains common pattern: {pattern}")
            score -= 20
            
    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        feedback.append("[!] Has repeated characters")
        score -= 10
        
    # Determine strength rating with ASCII art lock
    if score < 20:
        strength = ("Very Weak", "|-x-|")
    elif score < 40:
        strength = ("Weak", "|--o|")
    elif score < 60:
        strength = ("Moderate", "|-O-|")
    elif score < 80:
        strength = ("Strong", "|-O+|")
    else:
        strength = ("Very Strong", "|=O=|")
        
    score = max(0, min(100, score))
    return strength, feedback, score

def display_password_analysis(password: str) -> None:
    """Display a beautifully formatted analysis of password strength."""
    # Clear some space
    print("\n" * 2)
    
    # Show analyzing animation
    print("Analyzing password", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")
    
    strength, feedback, score = check_password_strength(password)
    
    # ASCII Art Banner
    print("""
    /===============================\\
    |    Password Strength Test    |
    \\===============================/
    """)
    
    # Display strength meter
    print(f"  Strength: {strength[0]} {strength[1]}")
    print(f"  Score: {score}/100")
    print("  " + "-" * 30)
    
    # Display strength bar using ASCII
    bar_length = 20
    filled = int(score / 100 * bar_length)
    bar = "#" * filled + "-" * (bar_length - filled)
    print(f"\n  [{bar}] {score}%")
    
    # Display feedback
    print("\n  >>> Feedback:")
    for point in feedback:
        print(f"    {point}")
    
    print("\n  " + "=" * 30 + "\n")

def main():
    print("""
    /================================\\
    |  Password Strength Checker v2  |
    \\================================/
    """)
    print("Enter 'q' to quit anytime\n")
    
    while True:
        password = input(">>> Enter password to check: ")
        if password.lower() == 'q':
            print("\nThanks for using Password Strength Checker!\n")
            break
        display_password_analysis(password)

if __name__ == "__main__":
    main()