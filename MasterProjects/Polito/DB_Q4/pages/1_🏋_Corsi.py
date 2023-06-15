import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata

def visualize_metric_courses():

    col1, col2 = st.columns(2)

    query = "SELECT COUNT(*) FROM CORSI"
    date = execute_query(st.session_state["connection"], query)
    n_courses = date.fetchone()[0]

    with col1:
        st.metric("Numero di corsi", value= n_courses)

    query = "with tab_raggruppamento_corsi as (SELECT Tipo FROM corsi GROUP BY Tipo) SELECT COUNT(*) FROM tab_raggruppamento_corsi"
    date = execute_query(st.session_state["connection"],query)
    type_courses = date.fetchone()[0]

    with col2:
        st.metric("Numero di corsi distinti",type_courses)
    pass

def visualize_tab_prenotazioni(query):
    date = execute_query(st.session_state["connection"], query)
    tab_prenotazioni = pd.DataFrame(date)
    st.dataframe(tab_prenotazioni, use_container_width=True)

if __name__ == "__main__":
    st.title("🏋 :orange[Corsi]")

    if check_connection():
        visualize_metric_courses()

        filter = st.text_input(label="Filtra per tipo di corso")
        min_lvl= 0
        max_lvl = 10
        lvl_range = st.slider("Seleziona l'intervallo di livelli che desideri visualizzare", min_lvl, max_lvl, (min_lvl, max_lvl))
        query = "SELECT Giorno, OraInizio, Durata, Sala, programma.CodC, corsi.Nome, corsi.Tipo, corsi.Livello FROM programma, corsi  WHERE corsi.CodC = programma.CodC "
        if filter != "":
            query = query + f" and corsi.Tipo = '{filter}' "

        query = query + f"and CORSI.Livello <= {lvl_range[1]} and CORSI.Livello>={lvl_range[0]}"

        visualize_tab_prenotazioni(query= query)

