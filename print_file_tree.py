import os

def print_file_tree(directory, prefix=""):
    """
    Recursively prints the file tree for the specified directory.

    :param directory: The root directory to start the file tree from.
    :param prefix: The prefix used for tree structure representation.
    """
    try:
        # List all files and directories in the current directory
        entries = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}[Permission Denied]: {directory}")
        return
    
    for index, entry in enumerate(entries):
        # Create full path for the entry
        full_path = os.path.join(directory, entry)
        # Check if the current entry is the last in the directory
        is_last = index == len(entries) - 1
        
        # Print the current entry
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry}")
        
        # If it's a directory, recurse into it
        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_file_tree(full_path, new_prefix)

if __name__ == "__main__":
    # Change this to the directory you want to print the file tree for
    root_directory = "."
    print(f"File Tree for: {os.path.abspath(root_directory)}")
    print_file_tree(root_directory)
