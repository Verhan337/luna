MEMORY_FILE = "conversation_history.txt"

def save_message(role, text):
    with open(MEMORY_FILE, "a") as f:
        f.write(f"{role}: {text}\n")

def get_history():
    try:
        with open(MEMORY_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""