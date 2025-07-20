from security import vault, consent, audit
from config import USER

def handle(intent, entities):
    if intent == "add_bank_account":
        password = input("Vault password: ")
        bank_creds = input("Enter your bank API credentials (stub): ")
        vault.save_credential("bank_creds", bank_creds, password)
        return "Bank account added to vault."
    if intent == "get_balance":
        password = input("Vault password: ")
        creds = vault.load_credential("bank_creds", password)
        if not creds:
            return "No bank account found or wrong password."
        # Stub: replace with real API call
        return "Bank balance: $10,000 (stub)"
    if intent == "send_money":
        if not consent.require_consent("send money from your bank account"):
            return "Consent denied."
        password = input("Vault password: ")
        creds = vault.load_credential("bank_creds", password)
        if not creds:
            return "No bank account found or wrong password."
        to_account = entities.get("to")
        amount = entities.get("amount")
        # Stub: replace with real API call
        audit.log_action(f"Sent ${amount} to {to_account}", USER)
        return f"Sent ${amount} to {to_account} (stub)"
    return "Unknown banking command."