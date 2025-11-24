import streamlit as st
import google.generativeai as genai
from PIL import Image
import json

img = Image.open("icon.png")

if "documentos" not in st.session_state:
    st.session_state.documentos = []

if "analizando" not in st.session_state:
    st.session_state.analizando = False

st.set_page_config(page_title="Seguros Bolivar | Prueba Tecnica", page_icon=img)

def ConfigGemini():
    apiKey = st.secrets["api"]["geminiKey"]
    genai.configure(api_key=apiKey)

def PreguntarGemini(archivo):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = """
Eres un sistema experto en clasificación y extracción estructurada de información.
INSTRUCCIONES:
1. CLASIFICACIÓN ESTRICTA (GATEKEEPER):
Analiza el contenido del documento. Debes clasificarlo EXCLUSIVAMENTE en una de estas categorías si cumple con las características típicas:
- "cedula" (Documento de identidad oficial).
- "acta_de_seguros" (Pólizas, certificados de cobertura).
- "contrato" (Acuerdos legales firmados entre partes).
SI EL DOCUMENTO NO ENCAJA CLARAMENTE EN LAS 3 ANTERIORES (por ejemplo: es una hoja de vida, una factura, una receta médica, una foto genérica o texto ilegible), DEBES CLASIFICARLO COMO:
- "NO_VALIDO"
2. EXTRACCIÓN Y FORMATO:
Extrae la información relevante según la categoría y formatéala como una única cadena de texto en MARKDOWN (usa viñetas, negritas para los títulos de los campos, etc.). No uses null en el texto, simplemente omite el campo si no existe.
Campos a buscar y formatear en el Markdown:
- Si es CÉDULA: Nombre completo, Numero documento, Fecha nacimiento, lugar expedicion, fecha expedicion.
- Si es ACTA DE SEGUROS: numero poliza, asegurado, aseguradora, fecha inicio, fecha fin, prima, tipo cobertura, valores asegurados.
- Si es CONTRATO: partes involucradas, objeto contrato, fecha firma, vigencia, obligaciones principales, valor contrato, clausulas relevantes.
- Si detectas cualquier otro dato crucial, agrégalo también al Markdown.
3. SALIDA:
Devuelve EXCLUSIVAMENTE un objeto JSON con la siguiente estructura exacta:
{
  "type": "nombre_de_la_categoria",
  "identificador": "Aqui va el numero documento, numero poliza o numero de contrato
  "datos_importantes": "Aquí va el string con todo el contenido extraído formateado en Markdown"
}
4. RESTRICCIONES:
- No incluyas texto fuera del JSON.
- El valor de "datos_importantes" debe ser un string válido.
"""
    
    respuesta = model.generate_content([
                    prompt,
                    {
                        "inline_data": {
                            "mime_type": archivo.type,
                            "data": archivo.read()
                        }
                    }
                ])
    respuestalimpia = respuesta.text.replace("```json", "").replace("```", "").strip()
    st.session_state.documentos.append(json.loads(respuestalimpia))
    st.session_state.analizando = False
    st.rerun()



def RenderDocumentos(nombreExpander,tipoDocumento):
    with st.expander(nombreExpander,expanded = True):
        for documento in st.session_state.documentos:
            if documento["type"] != tipoDocumento:
                return
            with st.expander(f"Documento - {documento["identificador"]}"):
                st.markdown(documento["datos_importantes"])

def main():
    ConfigGemini()
    st.title('Clasificación y extraccion de datos')
 
    with st.spinner("Analizando tu documento, por favor espera..."):
        archivo = st.file_uploader(
            "Sube el archivo a analizar",
            type=["pdf"],
            disabled= st.session_state.analizando
        )
        if archivo is None:
            st.warning("⚠️ Por favor sube un archivo antes de analizar.")

        btn = st.button("Analizar", disabled= st.session_state.analizando)


        if btn and archivo is not None:
            st.session_state.analizando = True
            st.rerun()
            
        if st.session_state.analizando and archivo is not None:
            PreguntarGemini(archivo)


    RenderDocumentos("Cédulas","cedula")
    RenderDocumentos("Actas de Seguros","acta_de_seguros")
    RenderDocumentos("Contratos","contrato")
    st.write(st.session_state.documentos)

if __name__ == '__main__':
    main()