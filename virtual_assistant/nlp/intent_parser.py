try:
    from transformers import pipeline
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    def parse_intent(text):
        # Use the classifier to get intent (stub: map sentiment to intent for demo)
        result = classifier(text)[0]
        label = result['label']
        # Map sentiment to intent for demo; in production, fine-tune a model for intent
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
        # Use sentiment as a fallback intent
        if label == "POSITIVE":
            return "greet", {"text": text}
        if label == "NEGATIVE":
            return "complaint", {"text": text}
        return "unknown", {"text": text}
except Exception as e:
    def parse_intent(text):
        # Fallback to keyword-based
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