import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import sys
import json

# Path to your Vosk model directory
MODEL_PATH = "models/vosk-model-small-en-us-0.15"

try:
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)
    q = queue.Queue()
    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    def listen():
        print("Listening (Vosk)...")
        with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16', channels=1, callback=callback):
            result = ""
            while True:
                data = q.get()
                if recognizer.AcceptWaveform(data):
                    res = json.loads(recognizer.Result())
                    result = res.get("text", "")
                    break
            print(f"You: {result}")
            return result
except Exception as e:
    def listen():
        print("[Vosk not available, using text input]")
        return input("You: ")