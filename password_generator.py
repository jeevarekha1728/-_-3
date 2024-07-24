import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("At least one character set must be selected")
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
