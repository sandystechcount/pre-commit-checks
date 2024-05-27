import os
import re
import sys


def is_valid_file_folder_name(name):
    # Regular expression to match only lowercase letters, numbers, and underscores
    return re.match(r"^[a-z0-9_]+$", name) is not None


def main():
    if len(sys.argv) < 2:
        print("Usage: verify_file_folder_names.py <directory>")
        return 1

    directory = sys.argv[1]

    invalid_names = []

    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            if not is_valid_file_folder_name(name):
                invalid_names.append(os.path.join(root, name))

    if invalid_names:
        print(f"Error: The following file or folder names are invalid:\n" + "\n".join(invalid_names))
        return 1

    print("All file and folder names are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
