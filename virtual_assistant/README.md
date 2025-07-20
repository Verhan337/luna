# Standalone Virtual Assistant (Jarvis-like)

A fully standalone, modular, and extensible virtual assistant that runs entirely on your machine. Features include offline speech recognition/synthesis, local AI for intent parsing, PC and phone control, web search, smart home integration, and more.

## Features
- Offline speech recognition (Vosk)
- Offline speech synthesis (pyttsx3)
- Local LLM for intent parsing (HuggingFace Transformers)
- Modular skill system (PC control, phone control, web search, smart home, scheduler, etc.)
- Android phone integration via ADB
- GUI (Tkinter) and CLI interfaces
- Desktop notifications
- Security/authentication
- Extensible plugin system

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download a Vosk model and place it in a `models` directory (see Vosk docs).
3. (Optional) Download a HuggingFace model for local intent parsing.
4. Run the assistant:
   ```bash
   python main.py
   ```

## Adding Skills
- Add new Python modules in the `skills/` directory.
- Register them in `plugin_loader.py`.

## Configuration
- Edit `config.py` for device and user settings.

## Security
- Authentication and permissions are managed in the `security/` directory.

---

**This project is under active development.**