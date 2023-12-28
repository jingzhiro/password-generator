import random
from char import chars

def generate_password(password_len):
    password_len = int(password_len)
    for i in range(8):
        passwords = ''
        for c in range(password_len):
            passwords += random.choice(chars)
        
        print(passwords)

def main():
    while True: 
        print("Hello, how many characters would you like your password to be?")
        password_len = input()

        if not password_len.isnumeric():
            print("Enter a numeric character!")
            continue

        print("Generated passwords:")
        generate_password(password_len)
        break

if __name__ == "__main__": 
    main()