from io.speech_input import listen
from io.speech_output import speak
from nlp.intent_parser import parse_intent
from skills.plugin_loader import load_skills, route_command

def main():
    speak("Hello! How can I help you?")
    skills = load_skills()
    while True:
        user_input = listen()
        if not user_input:
            continue
        intent, entities = parse_intent(user_input)
        if intent == "exit":
            speak("Goodbye!")
            break
        response = route_command(intent, entities, skills)
        speak(response)

if __name__ == "__main__":
    main()