import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from utils import copy_to_clipboard  # Import the shared function

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY is not set. Please configure it in the .env file.")
    exit(1)
client = OpenAI(api_key=api_key)

# Function to summarize text using OpenAI API
def summarize_text(client, text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that provides concise summaries of text files."},
            {"role": "user", "content": f"Summarize the following file content briefly: {text}"},
        ]
    )
    return response.choices[0].message.content.strip()

# Function to process files in a directory
def summarize_files_in_directory(directory, ignore_dirs=None, ignore_extensions=None):
    if ignore_dirs is None:
        ignore_dirs = ["node_modules", "__pycache__", "myenv"]
    if ignore_extensions is None:
        ignore_extensions = [".png", ".jpg", ".exe", ".dll"]

    file_summaries = []

    for root, dirs, files in os.walk(directory):
        # Skip ignored directories and hidden directories
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
                print(f"Summarizing file: {file_path}")  # Log the file being processed
                # Read file content
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Summarize file content
                summary = summarize_text(client, content[:3000])  # Limit content length for efficiency
                file_summaries.append({"file": file_path, "summary": summary})
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                file_summaries.append({"file": file_path, "summary": "Unable to process or summarize this file."})

    return file_summaries

# Main function
if __name__ == "__main__":
    # Prompt user for directory
    directory = input("Enter the path of the directory you want to summarize: ").strip()

    # Summarize files
    summaries = summarize_files_in_directory(directory)

    # Save summaries to a file
    output_file = os.path.join(directory, "file_summaries.json")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=4)
        print(f"\nSummaries saved to {output_file}")
    except Exception as e:
        print(f"Failed to save summaries: {e}")

    # Combine summaries into a single string
    combined_summaries = "\n\n".join(
        [f"File: {summary['file']}\nSummary:\n{summary['summary']}" for summary in summaries]
    )

    # Copy summaries to clipboard
    copy_to_clipboard(combined_summaries)
    print("\nAll summaries have been copied to your clipboard!")
    print("\nHere are the summaries:\n")
    print(combined_summaries)
