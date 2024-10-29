# -*- coding: utf-8 -*-
"""Alcohol.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uIFdsYUncffB1ig_TgYx_qVVI_v8XXH5
"""

import streamlit as st
from transformers import pipeline

# Título de la aplicación
st.title("Tu relación con el alcohol")
st.image("all.png",  width=200)



# Introducción
st.write("""
Esta aplicación tiene como objetivo compartir experiencias sobre el alcohol que hemos vivido.
""")

# Diccionario de términos con multimedia
terminos = {
    "Salud": {
        "descripcion": "No es necesario saber mucho acerca de medicina, para entender que te dañas tu higado.",
        "image": "al.png"
    },
    "Energía": {
        "descripcion": "Despues de una borrachera, pierdes mucha energía y ritmo de lo que venías haciendo.",
        "image": "al.png"
    },
    "Resaca": {
        "descripcion": "A tu edad te dura minimo tres días la cruda.",
        "image": "al.png"
    },
    "Cruda Moral": {
        "descripcion": "El sentirte mal por lo que hablaste de más o accionar incorrecto (en hechos y gastos)",
        "image": "al.png"
    },
    "Productividad": {
        "descripcion": "Tu productividad baja considerablemente, no hay mejor aliado que un cafecito (tu mejor compañero).",
        "image": "al.png"
    },
    "Memoria": {
        "descripcion": "Con el pasar del tiempo (por lo regular una semana o más) las consecuencias del alcohol se te olvidan y tu mente te engaña (facilmente) haciendote creer que te la pasarás muy bien.",
        "image": "al.png"
    },
    "Familia": {
        "descripcion": "La familia la descuidas y la lastimas, es la más afectada de tus actos bajo el influjo del alcohol.",
        "image": "al.png"
    },
    "Relaciones sentimentales": {
        "descripcion": "No logras concretar ninguna relación sentimental seria.",
        "image": "al.png"
    },
    "Dinero": {
        "descripcion": "Desperdicias mucho tu dinero,cuando en realidad cuesta mucho trabajo ganarlo.",
        "image": "al.png"
    },
    "Ahorro": {
        "descripcion": "Tus ahorro disminuye considerablemente o desaparece, por completo, y pasas a ser deudor",
        "image": "al.png"
    },
    "Amistad": {
        "descripcion": "La amistad en la fiesta no existe, si traes dinero amigos te sobrarán, pero si no estarás de nuevo solo.",
        "image": "al.png"
    },
    "Riesgo": {
        "descripcion": "En las relaciones de alcohol, siempre se está en constante peligro.",
        "image": "al.png"
    },
    "Metas": {
        "descripcion": "Tus metas y logros personales se dejan de cumplir, además de tu crecimiento personal.",
        "image": "al.png"
    },
}

# Menú desplegable para seleccionar un término
term_selected = st.selectbox("Selecciona un término:", list(terminos.keys()))

# Mostrar descripción y GIF del término seleccionado con tamaño ajustado
if term_selected in terminos:
    st.subheader(term_selected)
    st.write(terminos[term_selected]["descripcion"])
    # st.image(terminos[term_selected]["gif"], caption=f"GIF representativo de {term_selected}")
    st.image(terminos[term_selected]["image"])
# Personalización de diseño


st.title("Chatbot de Consejos para Mantenerse Sobrio con NLP")

# Carga del modelo NLP para generar respuestas
# Usa el pipeline de pregunta-respuesta para entender las consultas del usuario
nlp = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Base de conocimientos sobre la sobriedad
advice_data = """
Aquí tienes algunos consejos para mantenerte sobrio:
- Establece metas claras y alcanzables para tu proceso de sobriedad.
- Rodéate de personas que te apoyen y mantén una red de apoyo.
- Busca actividades saludables y que te mantengan ocupado.
- Considera asistir a reuniones de apoyo, como Alcohólicos Anónimos (AA).
- Recuerda tus motivos para permanecer sobrio, mantente enfocado.
- Practica el autocuidado: ejercicio, buena alimentación y descanso.
- Establece un sistema de recompensas para tus logros y avances.
- No salgas con dinero de más, puedes recaer.
- Evita frecuentar lugares donde acostumbras tomar.
- Recueda que la mente te engaña facilmente, mantente firme en tu sobriedad.
"""

def get_advice(question):
    # Usa el pipeline para generar una respuesta en función de la pregunta del usuario
    result = nlp(question=question, context=advice_data)
    return result["answer"]

# Entrada del usuario
user_query = st.text_input("Escribe tu pregunta o consulta sobre sobriedad:")
if user_query:
    response = get_advice(user_query)
    st.write("Chatbot:", response)

st.markdown("""
<style>
    .stApp {
        background-color:  #da3262;
    }
    .css-1d391kg {
        color:  #faf7f8;
    }
</style>
""", unsafe_allow_html=True)

# Añadir la línea separadora
st.markdown("<hr>", unsafe_allow_html=True)

# Sección de recursos adicionales
st.header("Recursos Adicionales")
st.write("Alcohólicos Anónimos® México")
st.write("https://www.aamexico.org.mx/")

# Añadir la línea separadora
st.markdown("<hr>", unsafe_allow_html=True)

# Insertar el código HTML con estilos personalizados
st.markdown("""
    <div class="container col-sm-5 creditos text-center">
        <p style="margin-top:0;margin-bottom:0;font-size:15px;color: #424040;text-align:center">
            <strong>Colaboración:</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>El Alex </strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>Mil y una fiestas</strong>
        </p>
    </div>
""", unsafe_allow_html=True)