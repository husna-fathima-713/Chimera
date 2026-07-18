from backend.rag.loader import DocumentLoader
from backend.rag.chunker import TextChunker

loader = DocumentLoader()
chunker = TextChunker()

text = loader.load("README.md")

chunks = chunker.split(text)

print(f"Chunks created: {len(chunks)}")

print()

print(chunks[0])

print()

print("-" * 80)

print()

if len(chunks) > 1:
    print(chunks[1])