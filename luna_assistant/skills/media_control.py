def handle(intent, entities):
    if intent == "play_media":
        file = entities.get("file", "")
        # Stub: replace with actual player command
        return f"Playing media: {file} (stub)"
    if intent == "pause_media":
        return "Pausing media (stub)"
    if intent == "stop_media":
        return "Stopping media (stub)"
    return "Unknown media control command."