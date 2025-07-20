def handle(intent, entities):
    if intent == "turn_on_light":
        return "Turning on the light (stub)."
    if intent == "turn_off_light":
        return "Turning off the light (stub)."
    if intent == "get_temperature":
        return "The current temperature is 22°C (stub)."
    return "Unknown smart home command."