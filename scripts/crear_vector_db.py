from app.services.pdf_service import cargar_pdf
from app.services.rag_service import dividir_documentos
from app.services.vector_service import crear_vectorstore

print("📄 Cargando PDF...")

ruta_pdf = "data/knowledge_base/ManitasF_Base_de_Conocimiento_LSM.pdf"

documentos = cargar_pdf(ruta_pdf)

print(f"✅ PDF cargado ({len(documentos)} páginas)")

print("✂️ Dividiendo en fragmentos...")

chunks = dividir_documentos(documentos)

print(f"✅ {len(chunks)} fragmentos creados")

print("🧠 Generando embeddings...")

crear_vectorstore(chunks)

print("🎉 Base vectorial creada correctamente.")