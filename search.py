import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading index...")
index = faiss.read_index("healthcare_index.faiss")

print("Loading papers...")
with open("papers.pkl", "rb") as f:
    papers = pickle.load(f)

def search(query, top_k=5):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # normalize (IMPORTANT for cosine similarity)
    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in range(len(indices[0])):
        idx = indices[0][i]
        paper = papers[idx]

        results.append({
            "title": paper.get("title", ""),
            "abstract": paper.get("abstract", ""),
            "score": float(distances[0][i])
        })

    return results


if __name__ == "__main__":
    while True:
        query = input("\n🔍 Search: ")
        if query.lower() == "exit":
            break

        results = search(query)

        print("\n📚 Top Results:\n")

        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']}")
            print(f"   Score: {r['score']:.4f}")
            print(f"   Abstract: {r['abstract'][:200]}...\n")