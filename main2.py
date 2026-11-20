# main1.py

from audioinput import record_audio
from speechmodule import speech_to_text, speak
from intentmodule import classify_query
from news import get_news
from wiki import WikiAssistant
from llamamodule import ask_llm
from wakeword import detect_wake_word

wiki_assistant = WikiAssistant()
def process_query(query):

    intent = classify_query(query)
    print(f"[DEBUG] Intent detected: {intent}")

    # Casual / greeting detection
    casual_words = ["hello", "hi", "how are you", "what's up", "hey"]

    if any(word in query for word in casual_words):
        return ask_llm(query)

    #  News
    if intent == "news":
        return get_news(query)

    # Wikipedia (only for clear factual questions)
    elif intent == "factual":
        result = wiki_assistant.get_summary(query)

        # fallback if wiki fails
        if "could not find" in result.lower():
            return ask_llm(query)

        return wiki_assistant.format_for_speech(result)

    #  Reasoning → LLaMA
    elif intent == "reasoning":
        return ask_llm(query)

    #  Default fallback
    else:
        return ask_llm(query)
# MAIN LOOP
def main():

    print("=== Voice Assistant Started ===")
    print("Say 'exit' to stop\n")

    while True:
        detect_wake_word()

        speak("Yes, how can I help you?")

        wav_file = record_audio(silence_threshold=0.01,silence_duration=1.8)
        query = speech_to_text(wav_file)

        response = process_query(query)

        speak(response)


# -------------------------------
if __name__ == "__main__":
    main()