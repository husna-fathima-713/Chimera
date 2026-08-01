import re


class MemoryExtractor:

    def extract(self, text):

        memories = []

        patterns = [

            (
                r"\bmy name is (.+)",
                lambda m: f"User's name is {m.group(1).strip().rstrip('.')}.",
            ),

            (
                r"\bi am studying (.+)",
                lambda m: f"User is studying {m.group(1).strip().rstrip('.')}.",
            ),

            (
                r"\bi study (.+)",
                lambda m: f"User studies {m.group(1).strip().rstrip('.')}.",
            ),

            (
                r"\bi work as (.+)",
                lambda m: f"User works as {m.group(1).strip().rstrip('.')}.",
            ),

            (
                r"\bmy favorite language is (.+)",
                lambda m: f"User's favorite language is {m.group(1).strip().rstrip('.')}.",
            ),

        ]

        lower_text = text.lower()

        for pattern, builder in patterns:

            match = re.search(pattern, lower_text)

            if match:

                memories.append(builder(match))

        return memories