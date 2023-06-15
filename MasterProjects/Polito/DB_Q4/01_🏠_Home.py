import streamlit as st
import streamlit.proto.Image_pb2

from utils.utils import *
import pymysql,cryptography

if __name__ == "__main__":
    st.set_page_config(
        page_title="Palestra",
        layout="wide",
        page_icon="💪",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://dbdmg.polito.it/',
            'Report a bug': "https://dbdmg.polito.it/",
            'About': "# Corso di *Basi di Dati*"
        }
    )

    with st.container():
        col1,col2=st.columns([3,2])
        with col1:
            st.title(":red[Gestione] di una palestra ")
            st.markdown("### Descrizione del :blue[Database]")
        with col2:
            image_path = "./images/polito_white.png"
            st.image(image_path, caption= "Carletto Davide 297286")

    with st.container():
        with open("./DescFiles/DB_Desc", "r") as DescFile:
            content = DescFile.read()

            words_colors = {"PALESTRA": "lime", "ISTRUTTORE": "orange", "CORSI": "orange", "PROGRAMMA": "orange"}

            content = color_content(content,words_colors)
            st.markdown(content, unsafe_allow_html=True)
        st.markdown("##### Di seguito la rappresentazione dello :violet[schema E-R]:")
        image_path = "./images/schema.png"
        url_link = "https://designer.polito.it"

        st.image(image_path)

        st.markdown("<div style = 'text-align: center;'> Made with <a  href="f"{url_link}> Designer</a> </div>", unsafe_allow_html=True)
