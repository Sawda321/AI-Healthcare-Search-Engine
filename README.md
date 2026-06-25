# 🩺 AI Healthcare Search Engine

An advanced, AI-powered semantic search engine designed to scan, filter, and retrieve relevant healthcare and medical research papers. Utilizing FAISS (Facebook AI Similarity Search) and embedding models, this project provides lightning-fast and context-aware search results.

## 🚀 Features
* **Semantic Search:** Understands the actual meaning and context of your health-related queries, not just keywords.
* **FAISS Indexing:** Uses `healthcare_index.faiss` for high-performance and efficient vector searching.
* **Smart Filtering:** Built-in scripts to filter out noisy data and pinpoint precise healthcare papers.
* **Interactive UI:** A clean interface powered by Streamlit/Flask (`app.py`) to easily search and explore results.

## 🛠️ Technology Stack
* **Language:** Python 3
* **AI & Vector Search:** FAISS (Facebook AI Similarity Search), Sentence-Transformers / Embeddings
* **Data Processing:** Pandas, Pickle (`papers.pkl`), JSON (`healthcare_papers.json`)
* **Web Framework:** Python Web UI (Flask / Streamlit)

## 📁 Project Structure
* `app.py` - Main application file to run the web interface.
* `search.py` & `load_data.py` - Core search logic and dataset loaders.
* `build_index.py` - Script used to generate the FAISS vector index.
* `filter_healthcare.py` - Data pre-processing and medical filtering script.
* `run_project.bat` - One-click batch file to run the project instantly on Windows.

## 💻 How to Run the Project
1. Clone the repository to your local system.
2. Install the required dependencies:
   ```bash
   pip install faiss-cpu sentence-transformers pandas
