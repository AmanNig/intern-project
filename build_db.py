# build_db.py

from pdf_reader import TarotPDFEmbedder

if __name__ == "__main__":
    embedder = TarotPDFEmbedder()
    embedder.build_vector_store()
