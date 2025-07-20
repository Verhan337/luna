import tkinter as tk
from nlp.intent_parser import parse_intent
from skills.plugin_loader import load_skills, route_command
from nlp.conversation_memory import save_message

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Assistant")
        self.text_area = tk.Text(root, height=20, width=60)
        self.text_area.pack()
        self.entry = tk.Entry(root, width=60)
        self.entry.pack()
        self.entry.bind('<Return>', self.process_input)
        self.skills = load_skills()
        self.text_area.insert(tk.END, "Assistant: Hello! How can I help you?\n")

    def process_input(self, event):
        user_input = self.entry.get()
        self.text_area.insert(tk.END, f"You: {user_input}\n")
        save_message("user", user_input)
        intent, entities = parse_intent(user_input)
        response = route_command(intent, entities, self.skills)
        self.text_area.insert(tk.END, f"Assistant: {response}\n")
        save_message("assistant", response)
        self.entry.delete(0, tk.END)

def start_gui():
    root = tk.Tk()
    gui = AssistantGUI(root)
    root.mainloop()