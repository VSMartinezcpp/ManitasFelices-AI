from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from app.services.pdf_service import cargar_pdf
from app.services.rag_service import dividir_documentos


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

CHROMA_PATH = Path("data/chroma")
PDF_PATH = Path("data/knowledge_base/Lenguaje_señas_LSM.pdf")


def crear_vectorstore(chunks):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_PATH)
    )


def cargar_vectorstore():

    # Si no existe la carpeta de la base vectorial, la creamos automáticamente
    if not CHROMA_PATH.exists():

        if not PDF_PATH.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo PDF: {PDF_PATH}"
            )

        print("📄 Creando base vectorial...")

        documentos = cargar_pdf(str(PDF_PATH))
        chunks = dividir_documentos(documentos)

        crear_vectorstore(chunks)

        print("✅ Base vectorial creada correctamente.")

    return Chroma(
        persist_directory=str(CHROMA_PATH),
        embedding_function=embeddings
    )