def handle(intent, entities):
    if intent == "add_event":
        return "Event added to calendar (stub)."
    if intent == "get_events":
        return "Today's events: (stub)"
    return "Unknown calendar command."