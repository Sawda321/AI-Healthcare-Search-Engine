import streamlit as st
import pandas as pd
import numpy as np
import re
import pickle
from collections import defaultdict
import math
import time

# --- STEP 1: Text Preprocessing (Required) ---
# Cleans the text by removing special characters and common stop words [cite: 38, 56]
def preprocess(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text).lower())
    words = text.split()
    # Basic stop words list to filter out common noise [cite: 56]
    stop_words = set(["the", "is", "and", "a", "in", "to", "of", "it", "with", "for", "on", "as", "an", "by", "at"])
    return [w for w in words if w not in stop_words]

# --- STEP 2: Inverted Index Implementation (Core Requirement) ---
# Maps terms to document IDs for efficient retrieval [cite: 16, 19, 20]
def build_inverted_index(papers):
    inverted_index = defaultdict(list)
    for idx, paper in enumerate(papers):
        # Combine title and abstract for comprehensive indexing [cite: 56]
        content = paper.get('title', '') + " " + paper.get('abstract', '')
        words = preprocess(content)
        # Using set(words) to ensure document IDs are added once per unique word
        for word in set(words):
            inverted_index[word].append(idx)
    return inverted_index

# --- STEP 3: Ranking Mechanism (TF-IDF) ---
# Ranks documents based on term frequency and significance 
def calculate_tfidf(query, inverted_index, total_docs):
    query_words = preprocess(query)
    scores = defaultdict(float)
    
    for word in query_words:
        if word in inverted_index:
            docs_with_word = inverted_index[word]
            # IDF Calculation: log(Total Documents / Documents containing term) [cite: 59]
            idf = math.log10(total_docs / len(docs_with_word))
            for doc_id in docs_with_word:
                # Basic TF implementation as per project logic [cite: 59]
                scores[doc_id] += idf 
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# --- STEP 4: Keyword Highlighting (Bonus Feature) ---
# Visually highlights query terms in search results [cite: 76]
def highlight_keywords(text, query):
    query_words = preprocess(query)
    for word in query_words:
        if len(word) > 2: # Ignore very short words to maintain readability
            pattern = re.compile(rf'\b({word})\b', re.IGNORECASE)
            text = pattern.sub(r'<mark style="background-color: #fff3cd; color: #000; border-radius: 2px;">\1</mark>', text)
    return text

# --- Streamlit UI Configuration [cite: 69] ---
st.set_page_config(page_title="Specialized Research Search Engine", layout="wide")

# Data Loading with Caching for Speed
@st.cache_resource
def load_all_data():
    with open("papers.pkl", "rb") as f:
        papers = pickle.load(f)
    index = build_inverted_index(papers)
    return papers, index

papers, inverted_index = load_all_data()

# --- Sidebar UI ---
st.sidebar.markdown("### ⚙️ Engine Metadata")
st.sidebar.info(f"📊 **Papers Indexed:** {len(papers):,}")
st.sidebar.markdown("---")
st.sidebar.markdown("**Logic Architecture:** [cite: 16]")
st.sidebar.code("Term → List[DocIDs]\nRanking: TF-IDF Score")

# --- Main Search Panel [cite: 74] ---
st.markdown("<h1 style='text-align: center;'>🔬 Specialized Research Search Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>Domain: AI & Healthcare Research Papers [cite: 7, 10]</p>", unsafe_allow_html=True)

# Input Section [cite: 22, 30]
query = st.text_input("🔍 Search Database", placeholder="e.g., Cancer Treatment, Neural Networks")

col1, col2 = st.columns([2, 2])
with col1:
    # Boolean logic selection as per requirements [cite: 23]
    search_type = st.radio("Search Logic", ["AND (Specific)", "OR (Ranked)"], horizontal=True)
with col2:
    top_k = st.slider("Results per page", 5, 50, 10)

st.markdown("---")

# --- Result Processing & Display [cite: 25, 27] ---
if query:
    start_time = time.time()
    query_words = preprocess(query)
    results = []
    
    if search_type == "AND (Specific)":
        # Boolean AND: Document must contain ALL query words [cite: 23]
        if query_words:
            sets = [set(inverted_index.get(w, [])) for w in query_words]
            common_ids = set.intersection(*sets) if sets else set()
            results = [(doc_id, 1.0) for doc_id in common_ids]
    else:
        # TF-IDF Ranking for OR queries [cite: 23, 27, 59]
        results = calculate_tfidf(query, inverted_index, len(papers))
    
    execution_time = time.time() - start_time

    if not results:
        st.warning("No results found. Please refine your keywords.")
    else:
        # Search stats similar to Google [cite: 70, 71, 75]
        st.markdown(f"<p style='color: #888;'>Showing {min(top_k, len(results))} of {len(results)} results ({execution_time:.4f} seconds)</p>", unsafe_allow_html=True)
        
        for doc_id, score in results[:top_k]:
            paper = papers[doc_id]
            title = paper.get('title', 'Untitled')
            abstract = paper.get('abstract', 'No content available.')
            
            # Apply highlighting for bonus credit [cite: 76]
            h_title = highlight_keywords(title, query)
            h_snippet = highlight_keywords(abstract[:300], query) # Short snippet 
            h_full = highlight_keywords(abstract, query)
            
            # Modern UI Result Card [cite: 69, 70]
            st.markdown(f"""
                <div style="background-color: #1e1e1e; padding: 15px; border-radius: 8px; border: 1px solid #333; margin-bottom: 15px;">
                    <h4 style="margin-bottom: 5px;"><a href="#" style="color: #8ab4f8; text-decoration: none;">📄 {h_title}</a></h4>
                    <span style="color: #34a853; font-size: 0.8rem; font-weight: bold;">Relevance: {score:.4f}</span>
                    <p style="color: #bdc1c6; font-size: 0.9rem; margin-top: 10px;">{h_snippet}...</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("Show Full Abstract"):
                st.markdown(f"<div style='color: #eee;'>{h_full}</div>", unsafe_allow_html=True)