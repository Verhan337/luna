import getpass
USERS = {"owner": "jarvis"}

def authenticate():
    user = input("Username: ")
    password = getpass.getpass("Enter assistant password: ")
    return USERS.get(user) == password

def add_user(username, password):
    USERS[username] = password
    return f"User {username} added."

def remove_user(username):
    if username in USERS:
        del USERS[username]
        return f"User {username} removed."
    return f"User {username} not found."

def voice_authenticate():
    # Stub for voiceprint authentication
    return True