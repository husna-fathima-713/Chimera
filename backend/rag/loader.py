from pathlib import Path


class DocumentLoader:

    SUPPORTED_TYPES = {
        ".txt",
        ".md",
        ".py",
        ".js",
        ".java",
        ".c",
        ".cpp",
        ".html",
        ".css",
    }

    def load(self, filepath):

        path = Path(filepath)

        if path.suffix.lower() not in self.SUPPORTED_TYPES:
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        with open(path, "r", encoding="utf-8") as file:
            return file.read()