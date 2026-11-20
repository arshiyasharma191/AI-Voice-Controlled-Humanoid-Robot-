from intentmodule import classify_query
from news import get_news
from wiki import WikiAssistant
from llamamodule import ask_llm

wiki = WikiAssistant()


def process_query(query):

    intent = classify_query(query)
    print(f"\n[DEBUG] Detected intent: {intent}")

    if intent == "news":
        return get_news(query)

    elif intent == "factual":
        result = wiki.get_summary(query)

        # fallback to LLM if wiki fails
        if "not find" in result.lower() or "no information" in result.lower():
            
            return ask_llm(query)

        return result

    elif intent == "reasoning":
        
        return ask_llm(query)

    else:
        return "Sorry, I couldn't understand."


# -------------------------------
# TEST LOOP
# -------------------------------

if __name__ == "__main__":

    print("=== AI Assistant ===")
    print("Type 'exit' to quit\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        response = process_query(query)

        print("\nAssistant:", response)
        print("-" * 50)