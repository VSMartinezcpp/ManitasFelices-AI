from app.services.vector_service import cargar_vectorstore


def buscar_contexto(pregunta, k=5):
    """
    Busca los fragmentos más relevantes del documento para responder
    la pregunta del usuario.
    """

    vectorstore = cargar_vectorstore()

    documentos = vectorstore.similarity_search(
        pregunta,
        k=k
    )

    if not documentos:
        return ""

    contexto = "\n\n".join(
        doc.page_content for doc in documentos
    )

    return contexto