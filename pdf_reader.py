# pdf_embedder.py

import pdfplumber
import chromadb
from config import PDF_PATHS, VECTOR_DB_DIR
from chromadb.utils import embedding_functions

class TarotPDFEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2", collection_name="tarot_cards"):
        self.chroma_client = chromadb.Client()
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embed_fn
        )

    def extract_paragraphs(self):
        paragraphs = []
        for path in PDF_PATHS:
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        chunks = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 40]
                        paragraphs.extend(chunks)
        return paragraphs

    def build_vector_store(self):
        paragraphs = self.extract_paragraphs()
        ids = [f"chunk_{i}" for i in range(len(paragraphs))]
        if self.collection.count() == 0:
            self.collection.add(documents=paragraphs, ids=ids)
            print(f"🔗 Indexed {len(paragraphs)} chunks from {len(PDF_PATHS)} PDFs.")
        else:
            print(f"ℹ️ Collection already contains {self.collection.count()} chunks.")

    def retrieve(self, query, top_k=3):
        result = self.collection.query(query_texts=[query], n_results=top_k)
        return result["documents"][0] if result["documents"] else []
