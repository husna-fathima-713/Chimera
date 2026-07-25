class TextChunker:

    def __init__(self, chunk_size=800):

        self.chunk_size = chunk_size

    def split(self, text):

        paragraphs = [
            p.strip()
            for p in text.split("\n\n")
            if p.strip()
        ]

        chunks = []

        current_chunk = ""

        for paragraph in paragraphs:

            if len(current_chunk) + len(paragraph) < self.chunk_size:

                current_chunk += paragraph + "\n\n"

            else:

                if current_chunk.strip():
                    chunks.append(current_chunk.strip())

                current_chunk = paragraph + "\n\n"

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks