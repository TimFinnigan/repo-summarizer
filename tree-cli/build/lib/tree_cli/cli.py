import os
from tree_cli.utils import copy_to_clipboard  # Replace with your actual `copy_to_clipboard` implementation


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


def main():
    import argparse

    parser = argparse.ArgumentParser(description="CLI tool to generate a file tree.")
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        default=".",
        help="The path of the directory to scan (default is the current directory).",
    )
    parser.add_argument(
        "-i",
        "--ignore",
        type=str,
        default="node_modules,.git,__pycache__,myenv",
        help="Comma-separated list of directories to ignore (default: node_modules,.git,__pycache__,myenv).",
    )
    args = parser.parse_args()

    directory = args.directory
    ignore_dirs = args.ignore.split(",")

    print(f"\nGenerating file tree for: {os.path.abspath(directory)}\n")
    file_tree_output = generate_file_tree(directory, ignore_dirs=ignore_dirs)

    file_tree_text = "\n".join(file_tree_output)
    print(file_tree_text)

    # Copy to clipboard (always happens)
    copy_to_clipboard(file_tree_text)
    print("\nFile tree has been copied to your clipboard!")


if __name__ == "__main__":
    main()
