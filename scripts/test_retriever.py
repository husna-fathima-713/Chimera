from backend.rag.retriever import Retriever

retriever = Retriever()

retriever.index_document("README.md")

results = retriever.search("What is Chimera?")

print("\nTop Result:\n")
print(results[0])