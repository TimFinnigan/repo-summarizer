import os

def print_file_tree(directory, prefix="", ignore_dirs=None):
    """
    Recursively prints the file tree for the specified directory, with an option to ignore certain directories.

    :param directory: The root directory to start the file tree from.
    :param prefix: The prefix used for tree structure representation.
    :param ignore_dirs: A list of directory names to ignore.
    """
    if ignore_dirs is None:
        ignore_dirs = []

    try:
        # List all files and directories in the current directory
        entries = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}[Permission Denied]: {directory}")
        return

    entries = [entry for entry in entries if entry not in ignore_dirs]  # Filter ignored directories

    for index, entry in enumerate(entries):
        # Create full path for the entry
        full_path = os.path.join(directory, entry)
        # Check if the current entry is the last in the directory
        is_last = index == len(entries) - 1

        # Print the current entry
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry}")

        # If it's a directory and not ignored, recurse into it
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_file_tree(full_path, new_prefix, ignore_dirs)

if __name__ == "__main__":
    # Change this to the directory you want to print the file tree for
    root_directory = "."
    # Add directories to ignore here
    ignore_list = ["node_modules", ".git", "__pycache__"]

    print(f"File Tree for: {os.path.abspath(root_directory)}")
    print_file_tree(root_directory, ignore_dirs=ignore_list)
