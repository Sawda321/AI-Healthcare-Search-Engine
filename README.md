# 🔬 AI Healthcare Research Paper Search Engine

## 📖 Overview

AI Healthcare Research Paper Search Engine is a semantic search system designed to help users efficiently discover relevant healthcare research papers using Artificial Intelligence techniques.

Unlike traditional keyword-based search engines, this system utilizes Sentence Transformers and FAISS vector indexing to perform semantic search, enabling users to retrieve research papers based on meaning and context rather than exact keyword matching.

---

## 🎯 Objectives

* Develop an intelligent healthcare research paper retrieval system.
* Implement semantic search using sentence embeddings.
* Provide fast and relevant search results through vector similarity search.
* Create an interactive and user-friendly web interface.

---

## 🚀 Features

* Semantic Search using AI Embeddings
* Fast Retrieval with FAISS Vector Index
* Relevance Score Ranking
* Interactive Streamlit Web Interface
* Adjustable Number of Search Results
* Full Abstract Viewing
* Real-Time Search Performance Display

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
Sentence Transformer
     │
     ▼
Query Embedding
     │
     ▼
FAISS Vector Search
     │
     ▼
Top Relevant Papers
     │
     ▼
Streamlit User Interface
```

---

## 🛠️ Technologies Used

| Technology            | Purpose                  |
| --------------------- | ------------------------ |
| Python                | Core Development         |
| Streamlit             | Web Interface            |
| FAISS                 | Vector Similarity Search |
| Sentence Transformers | Text Embeddings          |
| NumPy                 | Numerical Computation    |
| Pickle                | Data Serialization       |

---

## 📂 Project Structure

```text
AI-Healthcare-Search-Engine/
│
├── app.py
├── build_index.py
├── search.py
├── healthcare_papers.json
├── healthcare_index.faiss
├── papers.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses a healthcare research paper dataset collected from Kaggle. The dataset contains research paper titles and abstracts that are indexed for semantic retrieval.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sawda321/AI-Healthcare-Search-Engine.git
```

### Navigate to Project Directory

```bash
cd AI-Healthcare-Search-Engine
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

After running the command, open:

```text
http://localhost:8501
```

---

## 🔍 Example Search Queries

* diabetes prediction
* heart disease detection
* cancer diagnosis
* healthcare machine learning
* COVID forecasting

---

## 📈 Results

The system successfully retrieves healthcare research papers based on semantic similarity and ranks results according to relevance scores generated through vector similarity search.

---

## 🔮 Future Improvements

* AI-generated Paper Summaries
* Advanced Filtering Options
* Related Paper Recommendation System
* Citation Analysis
* Cloud Deployment
* Multi-Domain Research Search

---

## 📚 References

1. Kaggle Healthcare Research Paper Dataset
2. FAISS Documentation
3. Sentence Transformers Documentation
4. Streamlit Documentation
5. Manning, C. D., Raghavan, P., & Schütze, H. *Introduction to Information Retrieval*, Cambridge University Press, 2008.

---

## 👩‍💻 Author

**Sawda**

Department of Computer Science and Engineering

Academic Project – Information Retrieval & Search Engine
