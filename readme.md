# 📄 Clasificación y Extracción Automática de Información desde Documentos PDF  
### 🧠 Streamlit + Gemini 2.5 Flash

Este proyecto es una aplicación en **Python + Streamlit** que permite subir documentos PDF y obtener automáticamente:

- Clasificación del documento (Cédula, Acta de Seguros, Contrato, NO_VALIDO)
- Extracción estructurada de datos importantes en formato Markdown
- Almacenamiento y visualización de documentos analizados
- Integración con Google Gemini 2.5 Flash

---

## 🚀 Características principales

### 🔍 Clasificación inteligente
La IA identifica si el documento pertenece a una de las siguientes categorías:

- `cedula`
- `acta_de_seguros`
- `contrato`
- `NO_VALIDO` (si no encaja en ninguna categoría)

### 📝 Extracción avanzada de datos  
Dependiendo del tipo, la IA extrae información relevante.  
Ejemplos:

#### Para CÉDULA:
- Nombre completo  
- Número de documento  
- Fecha nacimiento  
- Lugar expedición  
- Fecha expedición  

#### Para ACTA DE SEGUROS:
- Número de póliza  
- Asegurado  
- Aseguradora  
- Fechas (inicio/fin)  
- Prima  
- Cobertura  
- Valores asegurados  

#### Para CONTRATO:
- Partes involucradas  
- Objeto  
- Fecha firma  
- Vigencia  
- Obligaciones  
- Valor  
- Cláusulas relevantes  

Además, la IA puede agregar datos adicionales relevantes.

### 🗂️ Interfaz organizada
Los documentos procesados se agrupan en:

- Cédulas  
- Actas de Seguros  
- Contratos  

Cada documento aparece dentro de un **expander** mostrando los datos extraídos.

### 🔐 Manejo seguro de credenciales
La API Key de Gemini se almacena en `.streamlit/secrets.toml`.

---

## 📁 Estructura del proyecto

