from langchain_community.document_loaders import PyPDFLoader


def cargar_pdf(ruta_pdf):
    loader = PyPDFLoader(ruta_pdf)
    return loader.load()