import re
from pathlib import Path

from backend.tools.base import BaseTool


class FileReaderTool(BaseTool):

    name = "file_reader"

    description = "Read a local text file."

    def can_handle(self, prompt):

        return bool(

            re.match(
                r"(read|open|show)\s+",
                prompt,
                re.IGNORECASE
            )

        )

    def prepare_input(self, prompt):

        match = re.search(

            r"(?:read|open|show)\s+(.+)",

            prompt,

            re.IGNORECASE

        )

        return match.group(1).strip()

    def execute(self, filepath):

        path = Path(filepath)

        if not path.exists():
            return "File not found."

        if path.is_dir():
            return "Path is a directory."

        try:

            return path.read_text(
                encoding="utf-8"
            )

        except Exception as e:

            return f"Error: {e}"