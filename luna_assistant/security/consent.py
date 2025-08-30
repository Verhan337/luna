def require_consent(action_desc):
    consent = input(f"Do you allow Luna to {action_desc}? (yes/no): ")
    return consent.strip().lower() == 'yes'