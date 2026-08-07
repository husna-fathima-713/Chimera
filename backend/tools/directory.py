from pathlib import Path
import re

from backend.tools.base import BaseTool


class DirectoryTool(BaseTool):

    name = "directory"

    description = "List files inside directories."

    def can_handle(self, prompt):

        prompt = prompt.lower()

        return (
            "list" in prompt
            or "directory" in prompt
            or "files" in prompt
            or "folder" in prompt
        )

    def prepare_input(self, prompt):

        match = re.search(

            r"(?:in|inside)\s+(.+)",

            prompt,

            re.IGNORECASE

        )

        if match:

            return match.group(1).strip()

        return "."

    def execute(self, directory):

        path = Path(directory)

        if not path.exists():

            return "Directory not found."

        if not path.is_dir():

            return "Not a directory."

        files = sorted(

            item.name

            for item in path.iterdir()

        )

        if not files:

            return "Directory is empty."

        return "\n".join(files)