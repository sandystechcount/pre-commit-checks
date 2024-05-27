import ast
import re
import sys


def get_class_names(script_path):
    with open(script_path, "r") as file:
        file_content = file.read()
    tree = ast.parse(file_content)
    class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return class_names


def is_pascal_case(name):
    return re.match(r"^[A-Z][a-zA-Z0-9]*$", name) is not None


def main():
    script_path = sys.argv[1]
    class_names = get_class_names(script_path)

    invalid_classes = [name for name in class_names if not is_camel_case(name)]

    if invalid_classes:
        print(f"Error: The following class names are not CamelCase: {', '.join(invalid_classes)}")
        return 1

    print("All class names are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
