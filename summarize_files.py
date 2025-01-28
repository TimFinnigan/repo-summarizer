import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logging.error("OPENAI_API_KEY is not set. Please configure it in the .env file.")
    exit(1)
client = OpenAI(api_key=api_key)

# Function to summarize text using OpenAI API
def summarize_text(client, text, filename):
    try:
        logging.info(f"Summarizing content of file: {filename}")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI that provides concise summaries of text files."},
                {"role": "user", "content": f"Summarize the following file content briefly: {text}"},
            ]
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        logging.error(f"Error summarizing file {filename}: {e}", exc_info=True)
        return f"Error summarizing file {filename}: {e}"

# Function to process files in a directory
def summarize_files_in_directory(directory, ignore_dirs=None, ignore_extensions=None):
    if ignore_dirs is None:
        ignore_dirs = ["node_modules", ".git", "__pycache__"]
    if ignore_extensions is None:
        ignore_extensions = [".png", ".jpg", ".exe", ".dll"]

    file_summaries = []

    for root, dirs, files in os.walk(directory):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]

            # Skip ignored file types
            if file_extension in ignore_extensions:
                continue

            try:
                # Read file content
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Summarize file content
                summary = summarize_text(client, content[:3000], file)  # Limit content length for efficiency
                file_summaries.append({"file": file_path, "summary": summary})
            except Exception as e:
                logging.error(f"Error processing file {file_path}: {e}")

    return file_summaries

# Main function
if __name__ == "__main__":
    # Prompt user for directory
    directory = input("Enter the path of the directory you want to summarize: ").strip()

    # Summarize files
    print(f"Summarizing files in directory: {directory}")
    summaries = summarize_files_in_directory(directory)

    # Save summaries to a file
    output_file = os.path.join(directory, "file_summaries.json")
    try:
        import json

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=4)
        print(f"Summaries saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving summaries: {e}")
        print("Failed to save summaries.")

    # Print summaries
    for summary in summaries:
        print(f"\nFile: {summary['file']}\nSummary:\n{summary['summary']}")
