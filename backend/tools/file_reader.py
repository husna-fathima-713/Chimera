from pathlib import Path
import re

from backend.tools.base import BaseTool


class FileReaderTool(BaseTool):

    name = "file_reader"

    description = "Read a text file."

    def can_handle(self, prompt):

        return bool(

            re.match(
                r"(read|open|show)",
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

        if match:

            return match.group(1).strip()

        return ""

    def execute(self, filepath):

        path = Path(filepath)

        if not path.exists():

            return "File not found."

        if path.is_dir():

            return "Path is a directory."

        try:

            lines = []

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                for i, line in enumerate(file):

                    if i >= 200:
                        break

                    lines.append(line.rstrip())

            result = "\n".join(lines)

            if len(lines) == 200:

                result += (
                    "\n\n...Output truncated..."
                )

            return result

        except Exception as e:

            return str(e)