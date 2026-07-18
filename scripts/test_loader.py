from backend.rag.loader import DocumentLoader

loader = DocumentLoader()

text = loader.load("README.md")

print(text[:500])