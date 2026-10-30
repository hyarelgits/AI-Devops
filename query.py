question = input("Ask Question: ")

result = collection.query(
    query_texts=[question],
    n_results=1
)

context = result["documents"][0][0]
