import platform
import subprocess

def copy_to_clipboard(text):
    system = platform.system()
    try:
        if system == "Windows":
            process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, text=True)
        elif system == "Darwin":  # macOS
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, text=True)
        elif system == "Linux":
            process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE, text=True)
        else:
            print("Clipboard copy not supported on this OS.")
            return
        process.communicate(input=text)
    except FileNotFoundError:
        print("Clipboard utility not found. Install 'xclip' on Linux or ensure clipboard commands are available.")
