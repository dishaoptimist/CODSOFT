import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not any([uppercase, lowercase, digits, special_chars]):
        raise ValueError("At least one character type should be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length_str = input("Enter the desired length of the password: ")
    if not length_str.isdigit() or int(length_str) <= 0:
        print("Error: Password length must be a positive integer.")
        return
    length = int(length_str)

    uppercase = input("Need uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Need lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Need digits? (y/n): ").lower() == 'y'
    special_chars = input("Need special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, lowercase, digits, special_chars)
    if password is not None:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()