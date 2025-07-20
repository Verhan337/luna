def parse_intent(text):
    # TODO: Replace with local LLM or spaCy-based intent parsing
    text = text.lower()
    if "create file" in text:
        return "create_file", {"filename": text.replace("create file", "").strip()}
    if "delete file" in text:
        return "delete_file", {"filename": text.replace("delete file", "").strip()}
    if "open app" in text:
        return "open_app", {"app": text.replace("open app", "").strip()}
    if "search for" in text:
        return "web_search", {"query": text.replace("search for", "").strip()}
    if "install app" in text:
        return "install_app", {"apk_path": text.replace("install app", "").strip()}
    if "remove app" in text:
        return "remove_app", {"package": text.replace("remove app", "").strip()}
    if "send sms to" in text:
        # Example: send sms to 1234567890: hello
        try:
            rest = text.replace("send sms to", "").strip()
            number, message = rest.split(":", 1)
            return "send_sms", {"number": number.strip(), "message": message.strip()}
        except Exception:
            return "send_sms", {"number": "", "message": ""}
    if "cpu info" in text:
        return "cpu_info", {}
    if "ram info" in text or "memory info" in text:
        return "ram_info", {}
    if "disk info" in text or "storage info" in text:
        return "disk_info", {}
    if "exit" in text or "quit" in text:
        return "exit", {}
    return "unknown", {"text": text}