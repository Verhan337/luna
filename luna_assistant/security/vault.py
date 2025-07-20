from cryptography.fernet import Fernet
import base64
import os
from config import VAULT_FILE

# Derive a Fernet key from a password (for demo, use password directly; in production, use PBKDF2)
def get_vault_key(password):
    # Pad/truncate password to 32 bytes for Fernet (not secure, for demo only)
    key = password.encode('utf-8')[:32].ljust(32, b'0')
    return base64.urlsafe_b64encode(key)

def save_credential(name, value, password):
    key = get_vault_key(password)
    f = Fernet(key)
    data = f.encrypt(value.encode('utf-8'))
    vault = {}
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, 'rb') as f_vault:
            vault = f.decrypt(f_vault.read())
            vault = eval(vault.decode('utf-8'))
    vault[name] = data.decode('utf-8')
    with open(VAULT_FILE, 'wb') as f_vault:
        f_vault.write(f.encrypt(str(vault).encode('utf-8')))

def load_credential(name, password):
    key = get_vault_key(password)
    f = Fernet(key)
    if not os.path.exists(VAULT_FILE):
        return None
    with open(VAULT_FILE, 'rb') as f_vault:
        vault = f.decrypt(f_vault.read())
        vault = eval(vault.decode('utf-8'))
    data = vault.get(name)
    if data:
        return f.decrypt(data.encode('utf-8')).decode('utf-8')
    return None