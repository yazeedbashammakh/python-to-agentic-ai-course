import json


def load_json(filename):
    """
    Load data from a JSON file.
    """

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_json(filename, data):
    """
    Save data to a JSON file.
    """

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)