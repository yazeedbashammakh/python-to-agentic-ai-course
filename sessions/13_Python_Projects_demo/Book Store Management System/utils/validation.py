def get_integer(message):
    """
    Get a valid integer from the user.
    """

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid integer.")


def get_float(message):
    """
    Get a valid decimal number from the user.
    """

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_string(message):
    """
    Get a non-empty string from the user.
    """

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


def confirm(message):
    """
    Ask the user for confirmation.
    """

    while True:

        choice = input(f"{message} (Y/N): ").strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter Y or N.")