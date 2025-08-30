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
        if "remind me at" in text:
            try:
                rest = text.split("remind me at", 1)[1].strip()
                time_part, message = rest.split("to", 1)
                return "set_reminder", {"time": time_part.strip(), "message": message.strip()}
            except Exception:
                return "set_reminder", {"time": "", "message": ""}
        if "cpu info" in text:
            return "cpu_info", {}
        if "ram info" in text or "memory info" in text:
            return "ram_info", {}
        if "disk info" in text or "storage info" in text:
            return "disk_info", {}
        if "exit" in text or "quit" in text:
            return "exit", {}
        if "turn on light" in text:
            return "turn_on_light", {}
        if "turn off light" in text:
            return "turn_off_light", {}
        if "temperature" in text:
            return "get_temperature", {}
        if "copy" in text and "to clipboard" in text:
            try:
                to_copy = text.split("copy",1)[1].split("to clipboard")[0].strip()
                return "copy_to_clipboard", {"text": to_copy}
            except Exception:
                return "copy_to_clipboard", {"text": ""}
        if "paste clipboard" in text or "paste from clipboard" in text:
            return "paste_from_clipboard", {}
        if "read clipboard" in text:
            return "read_clipboard", {}
        if text.startswith("play "):
            file = text.replace("play ", "").strip()
            return "play_media", {"file": file}
        if "pause media" in text:
            return "pause_media", {}
        if "stop media" in text:
            return "stop_media", {}
        if "add event" in text:
            return "add_event", {}
        if "what are my events" in text or "show calendar" in text:
            return "get_events", {}
        if "add wallet" in text:
            return "add_wallet", {}
        if "get crypto balance" in text or "get eth balance" in text:
            return "get_balance", {"type": "crypto"}
        if "send eth to" in text:
            try:
                rest = text.split("send eth to", 1)[1].strip()
                to, amount = rest.split("amount", 1)
                return "send_eth", {"to": to.strip(), "amount": amount.strip()}
            except Exception:
                return "send_eth", {"to": "", "amount": ""}
        if "swap tokens" in text:
            return "swap_tokens", {}
        if "add bank account" in text:
            return "add_bank_account", {}
        if "get bank balance" in text:
            return "get_balance", {"type": "bank"}
        if "send money to" in text:
            try:
                rest = text.split("send money to", 1)[1].strip()
                to, amount = rest.split("amount", 1)
                return "send_money", {"to": to.strip(), "amount": amount.strip()}
            except Exception:
                return "send_money", {"to": "", "amount": ""}
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
        if "remind me at" in text:
            try:
                rest = text.split("remind me at", 1)[1].strip()
                time_part, message = rest.split("to", 1)
                return "set_reminder", {"time": time_part.strip(), "message": message.strip()}
            except Exception:
                return "set_reminder", {"time": "", "message": ""}
        if "cpu info" in text:
            return "cpu_info", {}
        if "ram info" in text or "memory info" in text:
            return "ram_info", {}
        if "disk info" in text or "storage info" in text:
            return "disk_info", {}
        if "exit" in text or "quit" in text:
            return "exit", {}
        if "turn on light" in text:
            return "turn_on_light", {}
        if "turn off light" in text:
            return "turn_off_light", {}
        if "temperature" in text:
            return "get_temperature", {}
        if "copy" in text and "to clipboard" in text:
            try:
                to_copy = text.split("copy",1)[1].split("to clipboard")[0].strip()
                return "copy_to_clipboard", {"text": to_copy}
            except Exception:
                return "copy_to_clipboard", {"text": ""}
        if "paste clipboard" in text or "paste from clipboard" in text:
            return "paste_from_clipboard", {}
        if "read clipboard" in text:
            return "read_clipboard", {}
        if text.startswith("play "):
            file = text.replace("play ", "").strip()
            return "play_media", {"file": file}
        if "pause media" in text:
            return "pause_media", {}
        if "stop media" in text:
            return "stop_media", {}
        if "add event" in text:
            return "add_event", {}
        if "what are my events" in text or "show calendar" in text:
            return "get_events", {}
        if "add wallet" in text:
            return "add_wallet", {}
        if "get crypto balance" in text or "get eth balance" in text:
            return "get_balance", {"type": "crypto"}
        if "send eth to" in text:
            try:
                rest = text.split("send eth to", 1)[1].strip()
                to, amount = rest.split("amount", 1)
                return "send_eth", {"to": to.strip(), "amount": amount.strip()}
            except Exception:
                return "send_eth", {"to": "", "amount": ""}
        if "swap tokens" in text:
            return "swap_tokens", {}
        if "add bank account" in text:
            return "add_bank_account", {}
        if "get bank balance" in text:
            return "get_balance", {"type": "bank"}
        if "send money to" in text:
            try:
                rest = text.split("send money to", 1)[1].strip()
                to, amount = rest.split("amount", 1)
                return "send_money", {"to": to.strip(), "amount": amount.strip()}
            except Exception:
                return "send_money", {"to": "", "amount": ""}
        return "unknown", {"text": text}