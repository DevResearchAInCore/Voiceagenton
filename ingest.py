from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

def ingest_document(path):

    loader = PyPDFLoader(path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    db = FAISS.from_documents(docs, embeddings)

    db.save_local("vectorstore")

    print("Document indexed successfully")
