import adbutils

def handle(intent, entities):
    d = None
    try:
        d = adbutils.adb.device()
    except Exception as e:
        return f"No Android device found: {e}"
    if intent == "install_app":
        apk_path = entities.get("apk_path")
        if apk_path:
            try:
                d.install(apk_path)
                return f"App installed from {apk_path}."
            except Exception as e:
                return f"Error installing app: {e}"
        return "No APK path specified."
    elif intent == "remove_app":
        package = entities.get("package")
        if package:
            try:
                d.uninstall(package)
                return f"App '{package}' removed."
            except Exception as e:
                return f"Error removing app: {e}"
        return "No package specified."
    elif intent == "send_sms":
        number = entities.get("number")
        message = entities.get("message")
        if number and message:
            try:
                d.shell(["am", "start", "-a", "android.intent.action.SENDTO", "-d", f"smsto:{number}", "--es", "sms_body", message, "--ez", "exit_on_sent", "true"])
                return f"SMS sent to {number}."
            except Exception as e:
                return f"Error sending SMS: {e}"
        return "Number or message missing."
    return "Unknown phone control command."