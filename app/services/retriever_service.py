from app.services.vector_service import cargar_vectorstore


def buscar_contexto(pregunta, k=10):

    vectorstore = cargar_vectorstore()

    documentos = vectorstore.similarity_search(
        pregunta,
        k=k
    )

    contexto = "\n\n".join(
        doc.page_content for doc in documentos
    )

    return contexto