📄 Clasificación y Extracción Automática de Información desde Documentos PDF
🧠 Streamlit + Gemini 2.5 Flash

Este proyecto es una aplicación construida en Python con Streamlit que permite subir documentos PDF y obtener clasificación automática (Cédula, Acta de Seguros, Contrato) y extracción estructurada de datos, utilizando el modelo Gemini 2.5 Flash de Google.

La aplicación está diseñada para ser simple, rápida y completamente automática, ideal para validación documental, procesos administrativos o flujos de onboarding.

🚀 Características principales
🔍 1. Clasificación Inteligente

La IA determina si el documento es:

cedula

acta_de_seguros

contrato

NO_VALIDO (si no coincide con ninguna categoría)

📝 2. Extracción Avanzada de Datos

Dependiendo del tipo, la IA extrae y formatea los datos importantes en Markdown.

Ejemplos:

📘 Cédula

Nombre completo

Número de documento

Fecha y lugar de nacimiento

Lugar y fecha de expedición

🛡️ Acta de Seguros

Número de póliza

Asegurado

Aseguradora

Vigencia

Coberturas

Valores asegurados

📑 Contratos

Partes involucradas

Objeto del contrato

Obligaciones

Vigencia

Valor del contrato

Cláusulas relevantes

👉 Cualquier dato adicional relevante también se incluirá.

🗂️ 3. Interfaz organizada por categorías

Los documentos procesados aparecen agrupados en:

Cédulas

Actas de Seguros

Contratos

Cada documento muestra un expander con el contenido extraído.

🔐 4. Manejo seguro de API Key

La clave de Gemini se gestiona mediante:

.streamlit/secrets.toml


que NO debe subirse al repositorio.

🧠 Arquitectura interna

La aplicación usa st.session_state para manejar:

Variable	Descripción
documentos	Lista de documentos procesados
analizando	Estado que previene dobles análisis o múltiples clics
📁 Estructura del proyecto
📦 clasificador-documentos
 ┣ 📂 .streamlit
 ┃ ┗ 📄 secrets.toml   # No se sube
 ┣ 📄 app.py
 ┣ 📄 icon.png
 ┣ 📄 requirements.txt
 ┗ 📄 README.md

⚙️ Instalación

Clona el repositorio:

git clone https://github.com/tuusuario/tu_repo.git
cd tu_repo


Instala dependencias:

pip install -r requirements.txt

▶️ Ejecución
streamlit run app.py

🔐 Configuración de la API de Gemini

En la carpeta .streamlit crea:

secrets.toml
[api]
geminiKey = "TU_API_KEY_AQUI"


⚠️ Este archivo no debe subirse a GitHub.

✔️ Uso de la app

Subes un PDF

Presionas Analizar

La IA clasifica el documento

Extrae la información en formato Markdown

Se almacena y muestra organizado por tipo de documento

📷 Capturas (opcional)

Puedes añadir capturas como:

![Pantalla principal](screenshots/home.png)
![Resultado](screenshots/resultado.png)

🧪 Ejemplo de salida JSON generada por la IA
{
  "type": "cedula",
  "identificador": "1.098.765.432",
  "datos_importantes": "**Nombre completo:** Valentina Pérez\n**Fecha de nacimiento:** 1995-03-15\n..."
}

🛡️ Buenas prácticas y seguridad

No subas tu API Key a GitHub

Usa .gitignore para ignorar la carpeta .streamlit

Mantén el procesamiento dentro del backend local para evitar filtraciones

🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Pull requests, sugerencias y mejoras son apreciadas.

📝 Licencia

Libre uso para pruebas técnicas o desarrollos personales.