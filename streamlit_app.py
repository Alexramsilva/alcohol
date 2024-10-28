# -*- coding: utf-8 -*-
"""Alcohol.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uIFdsYUncffB1ig_TgYx_qVVI_v8XXH5
"""

import streamlit as st

# Título de la aplicación
st.title("Tu relación con el alcohol")
st.image("al.png", caption="UST-URC Universidad Rosario Castellanos", width=200)



# Introducción
st.write("""
Esta aplicación tiene como objetivo compartir mis experiencias sobre el alcohol que he vivido.
""")

# Diccionario de términos con multimedia
terminos = {
    "Salud": {
        "descripcion": "No es necesario saber mucho acerca de la medicina para entender que te dañas tu higado.",
        "image": "al.png"
    },
    "Energía": {
        "descripcion": "Despues de una borrachera, pierdes mucha energía y ritmode lo que venías haciendo.",
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
        "descripcion": "Tu productividad baja considerablemente, no hay mejor aliado que un cafecito (el mejor aliado).",
        "image": "al.png"
    },
    "Memoria": {
        "descripcion": "Con el pasar del tiempo (por lo regular una semana) las consecuencias del alcohol se te olvidan y la mente te engaña haciendote creer que te la pasarás muy bien.",
        "image": "al.png"
    },
    "Familia": {
        "descripcion": "La familia la descuidas la lastimas y es la más afectada de tus actos bajo elalcohol.",
        "image": "al.png"
    },
    "Relaciones sentimentales": {
        "descripcion": "No logras concretar ninguna relación sentimental seria.",
        "image": "al.png"
    },
    "Dinero": {
        "descripcion": "Desperdicias mucho tu dinero,eres muy dadivoso (cuando en realidad cuesta mucho trabajo ganarlo).",
        "image": "al.png"
    },
    "Ahorro": {
        "descripcion": "Tus ahorro disminuye considerablemente o desaparece, por completo, y pasas a ser deudor",
        "image": "al.png"
    },
    "Amistad": {
        "descripcion": "Laamistad en la fiesta no existe, si traes dinero amigos te sobrarán, pero si no estarás de nuevo solo.",
        "image": "al.png"
    },
    "Riesgo": {
        "descripcion": "En las relaciones de alcohol, siempre se está en constante peligro.",
        "image": "al.png"
    },
    "Metas": {
        "descripcion": "Tus metas y logros personales se dejan de cumplir,además de tu crecimiento personal.",
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
            <strong>Alex  LCFI-URC</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>Mil y una fiestas</strong>
        </p>
    </div>
""", unsafe_allow_html=True)