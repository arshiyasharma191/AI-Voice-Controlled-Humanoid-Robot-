# intent_module.py

from llamamodule import ask_llm


def classify_query(query):

    prompt = f"""
    Classify the user query into ONE category:
    news, factual, or reasoning.

    Query: {query}

    Answer only one word.
    """

    response = ask_llm(prompt).lower()

    if "news" in response:
        return "news"
    elif "reasoning" in response:
        return "reasoning"
    else:
        return "factual"


# -------------------------------
# TEST BLOCK
# -------------------------------

if __name__ == "__main__":

    print("=== Intent Module Test ===")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        intent = classify_query(query)

        print(f"\nDetected Intent: {intent}")
        print("-" * 40)