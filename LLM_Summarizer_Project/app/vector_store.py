# app/vector_store.py
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)  # 384 هو حجم الإخراج للنموذج

stored_texts = []  # لحفظ النصوص المرتبطة بالمتجهات

def store_text(text: str):
    embedding = model.encode([text])
    index.add(np.array(embedding, dtype=np.float32))
    stored_texts.append(text)

def search_similar(query: str, top_k=3):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding, dtype=np.float32), top_k)
    return [stored_texts[i] for i in I[0] if i < len(stored_texts)]

