import whisper
import pyttsx3

model = whisper.load_model("base")
engine = pyttsx3.init()


def speech_to_text(wav_file):
    result = model.transcribe(wav_file, language="en")
    text = result["text"]

    print("You:", text)
    return text.lower()


import time

def speak(text):
    print("Robot:", text)

    import pyttsx3
    engine = pyttsx3.init(driverName='sapi5')

    engine.say(text)
    engine.runAndWait()
    engine.stop()

    time.sleep(0.3)   #  prevents overlap issues
#test_code#
if __name__ == "__main__":

    from audioinput import record_audio

    while True:
        wav_file = record_audio()

        text = speech_to_text(wav_file)

        if "exit" in text:
            break

        speak(text)    