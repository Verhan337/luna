# Luna: Standalone AI Virtual Assistant

Luna is a fully standalone, modular, and extensible AI-powered virtual assistant that runs entirely on your machine. Luna can interact with your PC, phone, bank accounts, crypto wallets, and more—with your explicit consent. All sensitive credentials are stored securely in an encrypted local vault, and all sensitive actions are logged for your review.

## Features
- Offline speech recognition (Vosk)
- Offline speech synthesis (pyttsx3)
- Local LLM for intent parsing (HuggingFace Transformers)
- Modular skill system (PC, phone, banking, crypto, web, smart home, scheduler, etc.)
- Secure vault for credentials (encrypted, local)
- Explicit user consent for all sensitive actions
- Audit log for all sensitive actions
- Android phone integration via ADB
- GUI (Tkinter) and CLI interfaces
- Desktop notifications
- Security/authentication
- Extensible plugin system

## Secure Vault, Consent, and Audit
- **Vault:** All credentials (bank, crypto, etc.) are stored encrypted using your master password. Only decrypted in memory when needed.
- **Consent:** Luna will always ask for your explicit consent before using your sensitive info (bank, crypto, etc.).
- **Audit:** All sensitive actions are logged in an encrypted audit log for your review.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download a Vosk model and place it in a `models` directory (see Vosk docs).
3. (Optional) Download a HuggingFace model for local intent parsing.
4. Run Luna:
   ```bash
   python main.py
   ```

## Adding Skills
- Add new Python modules in the `skills/` directory.
- Register them in `plugin_loader.py`.

## Configuration
- Edit `config.py` for device and user settings.

## Security
- Authentication, permissions, vault, and audit are managed in the `security/` directory.

---

**This project is under active development.**