import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

papers = []
texts = []

print("Loading dataset...")

with open("healthcare_papers.json", "r", encoding="utf-8") as f:
    for line in f:
        try:
            paper = json.loads(line)
            papers.append(paper)

            texts.append(
                paper.get("title", "") + " " + paper.get("abstract", "")
            )
        except:
            continue

print(f"Total papers loaded: {len(papers)}")

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    convert_to_numpy=True
)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

print("Building FAISS index...")

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "healthcare_index.faiss")

with open("papers.pkl", "wb") as f:
    pickle.dump(papers, f)

print("DONE ✅ Index created successfully!")