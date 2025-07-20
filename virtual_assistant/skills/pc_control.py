import os
from utils import system_info
try:
    import pyperclip
except ImportError:
    pyperclip = None

def handle(intent, entities):
    if intent == "create_file":
        filename = entities.get("filename")
        if filename:
            try:
                with open(filename, "w") as f:
                    f.write("")
                return f"File '{filename}' created."
            except Exception as e:
                return f"Error creating file: {e}"
        return "No filename specified."
    elif intent == "delete_file":
        filename = entities.get("filename")
        if filename and os.path.exists(filename):
            try:
                os.remove(filename)
                return f"File '{filename}' deleted."
            except Exception as e:
                return f"Error deleting file: {e}"
        return "File not found."
    elif intent == "open_app":
        app = entities.get("app")
        if app:
            try:
                os.system(app + " &")
                return f"App '{app}' opened."
            except Exception as e:
                return f"Error opening app: {e}"
        return "No app specified."
    elif intent == "cpu_info":
        return system_info.get_cpu_info()
    elif intent == "ram_info":
        return system_info.get_ram_info()
    elif intent == "disk_info":
        return system_info.get_disk_info()
    elif intent == "copy_to_clipboard":
        if pyperclip:
            text = entities.get("text", "")
            pyperclip.copy(text)
            return "Copied to clipboard."
        return "Clipboard not available."
    elif intent == "paste_from_clipboard":
        if pyperclip:
            return f"Clipboard: {pyperclip.paste()}"
        return "Clipboard not available."
    elif intent == "read_clipboard":
        if pyperclip:
            return f"Clipboard: {pyperclip.paste()}"
        return "Clipboard not available."
    return "Unknown PC control command."