from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def crear_vectorstore(chunks):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/chroma"
    )


def cargar_vectorstore():
    return Chroma(
        persist_directory="data/chroma",
        embedding_function=embeddings
    )