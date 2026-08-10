from pathlib import Path

from backend.tools.base import BaseTool


class CodeSearchTool(BaseTool):

    name = "code_search"

    description = "Search inside source code."

    def can_handle(self, prompt):

        prompt = prompt.lower()

        return (
            prompt.startswith("find ")
            or prompt.startswith("where ")
            or prompt.startswith("search code")
        )

    def prepare_input(self, prompt):

        prompt = prompt.strip()

        for prefix in (
            "find ",
            "where ",
            "search code "
        ):

            if prompt.lower().startswith(prefix):

                return prompt[len(prefix):].strip()

        return prompt

    def execute(self, keyword):

        results = []

        for file in Path(".").rglob("*.py"):

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    for line_no, line in enumerate(f, start=1):

                        if keyword.lower() in line.lower():

                            results.append(

                                f"{file}:{line_no}: {line.strip()}"

                            )

            except Exception:

                continue

        if not results:

            return "No matches found."

        return "\n".join(results[:100])

    