from pathlib import Path
import re

from backend.tools.base import BaseTool


class SearchTool(BaseTool):

    name = "search"

    description = "Search for files by name."

    def can_handle(self, prompt):

        prompt = prompt.lower()

        return (
            "find" in prompt
            or "search" in prompt
            or "locate" in prompt
        )

    def prepare_input(self, prompt):

        match = re.search(

            r"(?:find|search|locate)\s+(.+)",

            prompt,

            re.IGNORECASE

        )

        if match:

            return match.group(1).strip()

        return ""

    def execute(self, keyword):

        root = Path(".")

        matches = []

        keyword = keyword.lower()

        for file in root.rglob("*"):

            if keyword in file.name.lower():

                matches.append(
                    str(file)
                )

        if not matches:

            return "No matching files found."

        return "\n".join(sorted(matches))