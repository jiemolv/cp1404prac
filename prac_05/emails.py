def extract_name(email):
    """Extracts a name from the email address"""
    name = email.split('@')[0]
    name = name.split('.')
    name = [part.capitalize() for part in name]
    return ' '.join(name)

def main():
    email_dict = {}
    while True:
        email = input("Email: ")
        if not email:
            break
        name = extract_name(email)
        print(f"Is your name {name}? (Y/n) ", end="")
        response = input().strip().lower()
        if response and response != "y":
            name = input("Name: ").strip()
        email_dict[email] = name

    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
