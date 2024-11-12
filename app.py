import streamlit as st 
from gtts import gTTS
import os
def create_audiobook (text, language, output_file):
    tts = gTTS(text=text, lang=language, tld='com')
    tts.save (output_file)
# Título de la Aplicación st.title("Generador de Audiolibros")
# Input del Texto
st.title('Text2Audio')
text = st. text_area("Introduce el texto aquí:")
languages = {
    "Español (es)": "es",
    "Inglés (en)": "en",
    "Francés (fr)": "fr",
    "Alemán (de)": "de"
}
language = st. selectbox("Selecciona el idioma:", list(languages. keys()))
# Lista Desplegable para el Acento
accents = {
    "com": "Estados Unidos",
    "co.uk": "Reino Unido",
    "ca": "Canadá",
    "com.au": "Australia",
    "co.in": "India"
}
accent = st.selectbox("Selecciona el acento:", list(accents.keys()))
if st.button ("Generar Audiolibro"):
    if text:
        output_file = "audiolibro.mp3"
        create_audiobook(text, languages [language], output_file)
        st. audio(output_file, format="audio/mp3")
    else:
        st.error ("Por favor, introduce un texto.")