from cryptography.fernet import Fernet
import base64
import os
from config import AUDIT_LOG_FILE

def get_audit_key():
    # For demo, use a static key. In production, use a secure key from user password or env.
    key = b'auditlogkeyauditlogkeyauditlogkey12'  # 32 bytes
    return base64.urlsafe_b64encode(key)

def log_action(action_desc, user):
    key = get_audit_key()
    f = Fernet(key)
    entry = f"{user}: {action_desc}\n"
    if os.path.exists(AUDIT_LOG_FILE):
        with open(AUDIT_LOG_FILE, 'rb') as f_log:
            data = f_log.read()
            try:
                decrypted = f.decrypt(data).decode('utf-8')
            except Exception:
                decrypted = ''
    else:
        decrypted = ''
    decrypted += entry
    with open(AUDIT_LOG_FILE, 'wb') as f_log:
        f_log.write(f.encrypt(decrypted.encode('utf-8')))