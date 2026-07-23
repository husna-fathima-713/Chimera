from pathlib import Path

from pypdf import PdfReader


class DocumentLoader:

    SUPPORTED_TYPES = {
        ".txt",
        ".md",
        ".pdf",
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

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_TYPES:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )

        if suffix == ".pdf":

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            return text

        with open(path, "r", encoding="utf-8") as file:
            return file.read()