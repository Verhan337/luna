try:
    import pyttsx3
    engine = pyttsx3.init()
    def speak(text):
        print(f"Assistant: {text}")
        engine.say(text)
        engine.runAndWait()
except Exception as e:
    def speak(text):
        print(f"Assistant: {text}")