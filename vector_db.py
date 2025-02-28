import os
import faiss
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure the necessary NLTK data files are downloaded
nltk.download('punkt')

class VectorDB:
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
        self.index = None
        self.documents = []
        self.doc_ids = []

    def load_documents(self):
        for filename in os.listdir(self.docs_path):
            if filename.endswith('.md'):
                with open(os.path.join(self.docs_path, filename), 'r', encoding='utf-8') as file:
                    self.documents.append(file.read())
                    self.doc_ids.append(filename)

    def create_index(self):
        tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        self.index = faiss.IndexFlatL2(tfidf_matrix.shape[1])
        self.index.add(tfidf_matrix.toarray().astype(np.float32))

    def search(self, query, top_k=5):
        query_vector = self.vectorizer.transform([query]).toarray().astype(np.float32)
        distances, indices = self.index.search(query_vector, top_k)
        results = [(self.doc_ids[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
        return results

if __name__ == "__main__":
    docs_path = './docs'
    vector_db = VectorDB(docs_path)
    vector_db.load_documents()
    vector_db.create_index()
    query = "What is data fabric?"
    results = vector_db.search(query)
    for doc_id, distance in results:
        print(f"Document: {doc_id}, Distance: {distance}")
