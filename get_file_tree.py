import os
from utils import copy_to_clipboard  # Import the shared function

def generate_file_tree(directory, prefix="", ignore_dirs=None, file_tree_list=None):
    if ignore_dirs is None:
        ignore_dirs = []

    if file_tree_list is None:
        file_tree_list = []

    try:
        entries = os.listdir(directory)
    except PermissionError:
        file_tree_list.append(f"{prefix}[Permission Denied]: {directory}")
        return file_tree_list
    except FileNotFoundError:
        file_tree_list.append(f"Error: The directory '{directory}' does not exist.")
        return file_tree_list

    entries = [entry for entry in entries if entry not in ignore_dirs]

    for index, entry in enumerate(entries):
        full_path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        file_tree_list.append(f"{prefix}{connector}{entry}")

        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            generate_file_tree(full_path, new_prefix, ignore_dirs, file_tree_list)

    return file_tree_list


if __name__ == "__main__":
    directory = input("Enter the path of the directory you want to scan: ").strip()
    ignored_input = input(
        "Enter directories to ignore (comma-separated, e.g., node_modules,.git), or press Enter to use defaults: "
    ).strip()
    ignore_dirs = ignored_input.split(",") if ignored_input else ["node_modules", "myenv", ".git", "__pycache__", "dist"]

    print(f"\nGenerating file tree for: {os.path.abspath(directory)}\n")
    file_tree_output = generate_file_tree(directory, ignore_dirs=ignore_dirs)

    file_tree_text = "\n".join(file_tree_output)
    print(file_tree_text)

    # Copy to clipboard
    copy_to_clipboard(file_tree_text)
    print("\nFile tree has been copied to your clipboard!")
