import os
import json
from dotenv import load_dotenv
from utils import copy_to_clipboard  # Import function for copying text

# Load environment variables
load_dotenv()

# Default ignore settings
IGNORE_DIRS = ["node_modules", "__pycache__", "myenv", "dist"]
IGNORE_EXTENSIONS = [".png", ".jpg", ".exe", ".dll", ".json"]

def read_files_in_directory(directory, ignore_dirs=None, ignore_extensions=None):
    """Reads all files in a directory while ignoring specified directories and extensions."""
    if ignore_dirs is None:
        ignore_dirs = IGNORE_DIRS
    if ignore_extensions is None:
        ignore_extensions = IGNORE_EXTENSIONS

    file_contents = []

    for root, dirs, files in os.walk(directory):
        # Remove ignored directories from search
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith(".")]

        for file in files:
            # Skip hidden files
            if file.startswith("."):
                continue

            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]

            # Skip ignored file types
            if file_extension in ignore_extensions:
                continue

            try:
                print(f"Reading file: {file_path}")  # Log progress

                # Read file content
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Store content with file path
                file_contents.append({"file": file_path, "content": content})
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                file_contents.append({"file": file_path, "content": "⚠️ Unable to read this file."})

    return file_contents

def format_as_markdown(file_contents):
    """Formats the file contents into Markdown format."""
    md_output = []
    
    for file_data in file_contents:
        relative_path = file_data["file"]
        content = file_data["content"]
        
        md_output.append(f"// {relative_path}\n\n{content}\n\n---\n")

    return "\n".join(md_output)

if __name__ == "__main__":
    # Get directory from user input
    directory = input("Enter the path of the directory you want to process: ").strip()

    # Read files
    files_data = read_files_in_directory(directory)

    # Format as markdown
    markdown_output = format_as_markdown(files_data)

    # Save to .md file
    output_file = os.path.join(directory, "files_output.md")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_output)
        print(f"\n✅ File contents saved to: {output_file}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")

    # Copy to clipboard
    copy_to_clipboard(markdown_output)
    print("\n📋 All file contents have been copied to clipboard!")

    # Print preview
    print("\n--- File Preview ---\n")
    print(markdown_output[:1000])  # Show first 1000 characters as a preview
    print("\n... (output truncated) ...")
