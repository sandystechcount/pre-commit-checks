import ast
import sys


def get_function_names(script_path):
    with open(script_path, "r") as file:
        file_content = file.read()
    tree = ast.parse(file_content)
    function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return function_names


def is_valid_method_name(name):
    special_methods = {"setUp", "runTest", "tearDown"}
    if name in special_methods:
        return True
    return name.islower() and "_" in name


def main():
    if len(sys.argv) < 2:
        print("Usage: verify_function_names.py <file>")
        return 1

    script_path = sys.argv[1]
    print(f"Script paths are: {script_path}")
    function_names = get_function_names(script_path)
    print(f"Following functions are checked: {function_names}")

    invalid_functions = [name for name in function_names if not is_valid_method_name(name)]

    if invalid_functions:
        print(f"Error: The following function names are not valid: {', '.join(invalid_functions)}")
        return 1

    print("All function names are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
