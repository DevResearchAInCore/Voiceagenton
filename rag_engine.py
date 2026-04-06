from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
import ollama
import os

def get_answer(question):

    if os.path.exists("vectorstore"):

        embeddings = OllamaEmbeddings(model="nomic-embed-text")

        db = FAISS.load_local(
            "vectorstore",
            embeddings,
            allow_dangerous_deserialization=True
        )

        docs = db.similarity_search(question, k=3)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Use the document context to answer.

Context:
{context}

Question:
{question}
"""

    else:

        prompt = f"""
Answer the question clearly.

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
