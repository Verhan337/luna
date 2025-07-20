import importlib
import os
from skills import pc_control, web_actions, phone_control, smart_home, scheduler, media_control, calendar

SKILLS_DIR = os.path.dirname(__file__)

def load_skills():
    # In the future, dynamically load all skills
    return {"pc_control": pc_control, "web_actions": web_actions, "phone_control": phone_control, "smart_home": smart_home, "scheduler": scheduler, "media_control": media_control, "calendar": calendar}

def load_plugins():
    plugins = {}
    for fname in os.listdir(SKILLS_DIR):
        if fname.endswith(".py") and fname not in ["__init__.py", "plugin_loader.py"]:
            modname = f"skills.{fname[:-3]}"
            try:
                mod = importlib.import_module(modname)
                plugins[fname[:-3]] = mod
            except Exception:
                pass
    return plugins

def route_command(intent, entities, skills):
    # Route to the appropriate skill based on intent
    if intent in ["create_file", "delete_file", "open_app", "cpu_info", "ram_info", "disk_info", "copy_to_clipboard", "paste_from_clipboard", "read_clipboard"]:
        return skills["pc_control"].handle(intent, entities)
    if intent == "web_search":
        return skills["web_actions"].handle(intent, entities)
    if intent in ["install_app", "remove_app", "send_sms"]:
        return skills["phone_control"].handle(intent, entities)
    if intent in ["turn_on_light", "turn_off_light", "get_temperature"]:
        return skills["smart_home"].handle(intent, entities)
    if intent == "set_reminder":
        return skills["scheduler"].handle(intent, entities)
    if intent in ["play_media", "pause_media", "stop_media"]:
        return skills["media_control"].handle(intent, entities)
    if intent in ["add_event", "get_events"]:
        return skills["calendar"].handle(intent, entities)
    return "Sorry, I don't know how to do that yet."