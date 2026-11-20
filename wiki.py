import wikipediaapi

class WikiAssistant:
    def __init__(self, language='en'):
        self.wiki = wikipediaapi.Wikipedia(
            language=language,
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent="MyRobotAssistant/1.0"
        )

    def get_summary(self, query, sentences=3):
        """
        Returns a clean summary suitable for speaking
        """
        page = self.wiki.page(query)

        if not page.exists():
            return "Sorry, I could not find any such information."

        summary = page.summary

        # Limit to first few sentences for speech
        summary_sentences = summary.split('. ')
        short_summary = '. '.join(summary_sentences[:sentences])

        return short_summary.strip()

    def get_full_content(self, query, char_limit=1000):
        """
        Returns longer content (useful for display/logging)
        """
        page = self.wiki.page(query)

        if not page.exists():
            return "No detailed content found."

        return page.text[:char_limit]

    def get_sections(self, query):
        """
        Returns section titles (for advanced bots)
        """
        page = self.wiki.page(query)

        if not page.exists():
            return []

        return [section.title for section in page.sections]

    def format_for_speech(self, text):
        """
        Cleans text to make it TTS-friendly
        """
        text = text.replace('\n', ' ')
        text = text.replace('  ', ' ')
        return text


# ---------------------------
# TEST PROGRAM (CLI BASED)
# ---------------------------

if __name__ == "__main__":

    assistant = WikiAssistant()

    print("=== Wikipedia Assistant ===")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        result = assistant.get_summary(query)
        result = assistant.format_for_speech(result)

        print("\nAnswer:\n", result)
        print("-" * 50)