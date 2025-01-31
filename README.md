# File Tree Generator, File Summarization, and Content Export

This project provides three powerful utilities for working with directories and files:

1. **File Tree Generator (`get_file_tree.py`)**: Quickly generate and share a visual representation of a directory's structure.
2. **File Summarization (`summarize_files.py`)**: Automatically generate concise summaries of files in a directory using the OpenAI API.
3. **File Content Export (`read_files.py`)**: Export all file contents from a directory into a single Markdown file with automatic clipboard copy.

---

## Features

### 1. File Tree Generator
- Recursively scans a directory and generates a visual file tree representation.
- Ignores hidden files and directories (e.g., `.git`, `.env`) by default.
- Allows user-defined directories to be excluded (e.g., `node_modules`).
- Copies the file tree to the clipboard for quick sharing.

### 2. File Summarization
- Summarizes the content of files in a directory using the OpenAI API.
- Ignores hidden files, specific directories (e.g., `node_modules`), and unsupported file types (e.g., `.png`, `.exe`).
- Saves the summaries to a JSON file and copies all summaries to the clipboard.

### 3. File Content Export
- Reads and exports the content of all files in a directory to a single Markdown file.
- Features:
  - Automatically skips binary files and specified file extensions.
  - Ignores specified directories (e.g., `node_modules`, `__pycache__`).
  - Formats output with file paths and content separators.
  - Copies all content to clipboard for easy sharing.

---

## Project Structure

```
/project
├── utils.py             # Shared utilities (e.g., `copy_to_clipboard` function)
├── get_file_tree.py     # Script for generating a file tree
├── summarize_files.py   # Script for generating file summaries
└── read_files.py      # Script for exporting file contents to Markdown
```

### File Descriptions

#### `utils.py`
- **`copy_to_clipboard(text)`**: Copies a given string to the clipboard. Works on Windows, macOS, and Linux (requires `xclip` on Linux).

#### `get_file_tree.py`
- Recursively scans a directory to generate a file tree representation.
- Outputs:
  - A printed file tree in the console.
  - The file tree text copied to the clipboard.
- Allows user to specify directories to ignore (e.g., `node_modules`, `.git`).

#### `summarize_files.py`
- Summarizes the content of files in a directory using OpenAI's GPT-4 model.
- Outputs:
  - A JSON file (`file_summaries.json`) containing all summaries.
  - All summaries combined into a single text string, copied to the clipboard.

#### `read_files.py`
- Reads and exports the content of all files in a directory to a single Markdown file.
- Features:
  - Automatically skips binary files and specified file extensions.
  - Ignores specified directories (e.g., `node_modules`, `__pycache__`).
  - Formats output with file paths and content separators.
  - Copies all content to clipboard for easy sharing.
- Outputs:
  - A Markdown file (`files_output.md`) containing all file contents.
  - All file contents copied to clipboard in Markdown format.

---

## Setup Instructions

### Prerequisites
1. **Python 3.7+** installed on your system.
2. **Install required Python packages**:
   ```bash
   pip install openai python-dotenv
   ```

3. **Linux Users**: Ensure `xclip` is installed for clipboard functionality:
   ```bash
   sudo apt install xclip
   ```

4. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## How to Use

### 1. File Tree Generator (`get_file_tree.py`)
#### Run the Script
```bash
python get_file_tree.py
```

#### Steps:
1. Enter the path of the directory you want to scan.
2. Optionally, specify directories to ignore (comma-separated).
3. The script will:
   - Generate a file tree and print it to the console.
   - Copy the file tree to the clipboard.

#### Example Output:
Console:
```
Generating file tree for: /example

├── file1.txt
├── file2.py
└── folder1
    ├── file3.md
    └── subfolder1
        └── file4.txt

File tree has been copied to your clipboard!
```

Clipboard:
```
├── file1.txt
├── file2.py
└── folder1
    ├── file3.md
    └── subfolder1
        └── file4.txt
```

---

### 2. File Summarization (`summarize_files.py`)
#### Run the Script
```bash
python summarize_files.py
```

#### Steps:
1. Enter the path of the directory you want to summarize.
2. The script will:
   - Summarize all files in the directory (excluding ignored ones).
   - Save the summaries to a `file_summaries.json` file.
   - Copy all summaries to the clipboard.

#### Example Output:
Console:
```
Summarizing file: /example/file1.txt
Summarizing file: /example/file2.py

Summaries saved to /example/file_summaries.json

All summaries have been copied to your clipboard!

Here are the summaries:

File: /example/file1.txt
Summary:
This file contains project notes and high-level ideas.

File: /example/file2.py
Summary:
This Python script automates data processing and file generation.
```

Clipboard:
```
File: /example/file1.txt
Summary:
This file contains project notes and high-level ideas.

File: /example/file2.py
Summary:
This Python script automates data processing and file generation.
```

---

### 3. File Content Export (`read_files.py`)
#### Run the Script
```bash
python read_files.py
```

#### Steps:
1. Enter the path of the directory you want to process.
2. The script will:
   - Read all compatible files in the directory (excluding ignored ones).
   - Generate a Markdown file with all contents.
   - Copy all contents to the clipboard.
   - Show a preview of the output.

#### Example Output:
Console:
```
Reading file: /example/file1.txt
Reading file: /example/file2.py

✅ File contents saved to: /example/files_output.md

📋 All file contents have been copied to clipboard!

--- File Preview ---

// /example/file1.txt

This is the content of file1.txt

---

// /example/file2.py

def hello_world():
    print("Hello, World!")

---

... (output truncated) ...
```

Markdown File (`files_output.md`):
```markdown
// /example/file1.txt

This is the content of file1.txt

---

// /example/file2.py

def hello_world():
    print("Hello, World!")

---
```

---

## Customization

### Ignored Files and Directories
- All scripts skip hidden files and directories (those starting with `.`) by default.
- You can customize the ignored directories or file extensions:
  - **`get_file_tree.py`**: Modify `ignore_dirs` in the `generate_file_tree` function or pass it as input when prompted.
  - **`summarize_files.py`**: Modify `ignore_dirs` or `ignore_extensions` in the `summarize_files_in_directory` function.
  - **`read_files.py`**: Modify `IGNORE_DIRS` or `IGNORE_EXTENSIONS` at the top of the script.

### OpenAI API Configuration
- Modify the OpenAI model used in `summarize_text` by changing the `model` parameter (default is `gpt-4`).

---

## Troubleshooting

### Common Errors:
1. **Clipboard Utility Not Found** (Linux):
   - Ensure `xclip` is installed:
     ```bash
     sudo apt install xclip
     ```

2. **OpenAI API Key Missing**:
   - Check if your `.env` file is properly set up with the `OPENAI_API_KEY`.

3. **File Summarization Errors**:
   - Ensure the file being summarized is a readable text file.
   - The script skips unsupported file types (e.g., binary files).

---

## Future Enhancements
- Add support for summarizing specific file types (e.g., `.md`, `.csv`).
- Add more visualization options for the file tree (e.g., export as JSON or HTML).
- Optimize API usage to handle larger directories efficiently.