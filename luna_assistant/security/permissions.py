SENSITIVE_ACTIONS = {"delete_file", "remove_app", "install_app"}

ALLOWED_USERS = {"owner"}  # Extend as needed

def is_permitted(user, intent):
    if intent in SENSITIVE_ACTIONS:
        return user in ALLOWED_USERS
    return True