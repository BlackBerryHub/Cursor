import re


def replace_by_pattern(input_str, target_word):
    """
    The user enters text from the keyboard, and a word, you need to count how many times it
    occurs in the text and replace it with the same word but with uppercase

    :param input_str:
    :param target_word:
    :return: (count, text)
    """
    pattern = re.compile(re.escape(target_word), re.IGNORECASE)
    count = len(pattern.findall(input_str))
    output_str = pattern.sub(target_word.upper(), input_str)
    return count, output_str


def validate_password(password):
    """
    Write a regular expression for password validation:
    - the password must be 8 characters minimum,
    - must contain upper and lower case letters, numbers, and special characters

    :param password:
    :return: True or False, [Errors]
    """
    errors = []
    if len(password) < 8:
        errors.append("Password too short - must be at least 8 characters")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one digit")
    if not re.search(r"[@$!%*?&]", password):
        errors.append("Password must contain at least one special character")

    if len(errors) >= 1:
        return False, errors
    else:
        return True


if __name__ == "__main__":
    while True:
        choice = input("Enter 1 (validate_password) or 2 (replace_by_pattern): ")

        if choice == "1":
            while True:
                print("Enter your password:")
                print(validate_password(input()))

        elif choice == "2":
            input_str = input("Enter some text: ")
            target_word = input("Enter a word to count and replace: ")

            count, output_str = replace_by_pattern(input_str, target_word)

            print(f"Count of '{target_word}' in input: {count}")
            print(f"Output string with '{target_word}' replaced: {output_str}")

        else:
            print("Invalid choice. Please enter 1 or 2.")

