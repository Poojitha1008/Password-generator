import random
import string

def generate_password(length=12, include_letters=True, include_digits=True, include_special_chars=True):
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available to generate a password")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter the password length: "))
    include_letters = input("Include letters? (yes/no): ").lower() in ["yes", "y"]
    include_digits = input("Include digits? (yes/no): ").lower() in ["yes", "y"]
    include_special_chars = input("Include special characters? (yes/no): ").lower() in ["yes", "y"]

    try:
        password = generate_password(length, include_letters, include_digits, include_special_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
