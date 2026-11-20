import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()

model = Model("vosk_model")
recognizer = KaldiRecognizer(model, 16000)

WAKE_WORDS = ["hey minidora", "hello minidora", "ok minidora","hi minidora", "hello many dora", "ok many dora","hi many dora","hey many dora","Namaste minidora","namaste many dora", "hey robot", "hello"]


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def detect_wake_word():
    print(" Waiting for wake word...")

    with sd.RawInputStream(samplerate=16000, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):

        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")

                if text:
                    print("Heard:", text)

                    if any(word in text for word in WAKE_WORDS):
                        print(" Wake word detected!")
                        return True