import random
import string

def generate_password(length):
    if length < 4:
        return "Password lenght should be at least 4 characters"
    
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def main():
    print("Generate your secret password here!")
    try:
        lenght = int(input("Enter the desired lenght of the password:"))
        password = generate_password(lenght)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
