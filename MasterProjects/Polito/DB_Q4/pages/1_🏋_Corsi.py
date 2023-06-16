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

def visualize_tab_corsi(query):
    date = execute_query(st.session_state["connection"], query)
    tab_corsi = pd.DataFrame(date)
    if tab_corsi.empty:
        return False
    st.dataframe(tab_corsi, use_container_width=True)
    return True

def visualize_tab_lezioni(query):
    date = execute_query(st.session_state["connection"], query)
    tab_lezioni = pd.DataFrame(date)
    if tab_lezioni.empty:
        return False
    st.dataframe(tab_lezioni, use_container_width=True)
    return True

if __name__ == "__main__":
    st.title("🏋 :orange[Corsi]")

    if check_connection():
        visualize_metric_courses()

        filter = st.text_input(label="Filtra per tipo di corso")
        min_lvl= 0
        max_lvl = 10
        lvl_range = st.slider("Seleziona l'intervallo di livelli che desideri visualizzare", min_lvl, max_lvl, (min_lvl, max_lvl))
        query = "SELECT Giorno, OraInizio, Durata, Sala, programma.CodC, corsi.Nome, corsi.Tipo, corsi.Livello FROM programma, corsi  WHERE corsi.CodC = programma.CodC "
        query2 = f"SELECT * FROM CORSI WHERE LIVELLO <= {lvl_range[1]} and Livello>={lvl_range[0]} "

        if filter != "":
            query = query + f" and corsi.Tipo = '{filter}' "
            query2 = query2 + f"AND TIPO = '{filter}'"

        query = query + f"and CORSI.Livello <= {lvl_range[1]} and CORSI.Livello>={lvl_range[0]}"

        st.write("Corsi selezionati:")
        if visualize_tab_corsi(query2):
            st.write("Lezioni che corrispondono ai corsi selezionati:")

            if(not visualize_tab_lezioni(query=query)):
                st.error("Non ci sono lezioni che corrispondono ai corsi selezionati.", icon='⚠️')
        else:
            st.error("Non ci sono corsi che corrispondono ai criteri di ricerca.", icon='⚠️')


