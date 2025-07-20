import getpass

def authenticate():
    password = getpass.getpass("Enter assistant password: ")
    # For demo, password is 'jarvis'. In production, use config or env var.
    return password == "jarvis"