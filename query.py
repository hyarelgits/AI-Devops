
import chromadb
import subprocess

# Ask user for question
question = input("Ask Question: ")

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="../chroma_db"
)

# Open collection
collection = client.get_collection(
    "enterprise_docs"
)

# Search relevant document
result = collection.query(
    query_texts=[question],
    n_results=1
)

# Get matching document
context = result["documents"][0][0]

print("\n========================")
print("CONTEXT FOUND:")
print("========================")
print(context)

# Build prompt
prompt = f"""
Answer using this context only.

Context:
{context}

Question:
{question}
"""

# Send to Qwen
subprocess.run(
    [
        "ollama",
        "run",
        "qwen2.5:3b",
        prompt
    ]
)
