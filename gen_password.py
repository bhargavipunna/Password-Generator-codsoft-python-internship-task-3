import random
import string


def password_generator(length, use_uppercase, use_numbers, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Ensure the password includes at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill the remaining length with random choices from the character pool
    password.extend(random.choice(chars) for _ in range(length - len(password)))

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)


def get_user_input(prompt, min_value=None, max_value=None, valid_responses=None):
    while True:
        response = input(prompt).strip().lower()

        # Handle yes/no responses
        if valid_responses and response in valid_responses:
            return valid_responses[response]

        # Handle numerical responses
        if min_value is not None:
            try:
                value = int(response)
                if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                    return value
                print(f"Please enter a number between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid response. Please try again.")


def main():
    print("🔒 Welcome to the Ultimate Password Generator 🔒")
    print("-------------------------------------------------")

    # Get password length from the user
    length = get_user_input(
        prompt="Enter the desired password length (minimum 4): ",
        min_value=4
    )

    # Get preferences for password complexity
    use_uppercase = get_user_input(
        prompt="Include uppercase letters? (yes/no): ",
        valid_responses={'yes': True, 'no': False}
    )
    use_numbers = get_user_input(
        prompt="Include numbers? (yes/no): ",
        valid_responses={'yes': True, 'no': False}
    )
    use_special_chars = get_user_input(
        prompt="Include special characters? (yes/no): ",
        valid_responses={'yes': True, 'no': False}
    )

    # Generate the password
    password = password_generator(length, use_uppercase, use_numbers, use_special_chars)

    print(f"\n🎉 Your Secure Password: {password} 🎉")
    print("Remember: Keep it safe and unique for each use!")


if __name__ == "__main__":
    main()
