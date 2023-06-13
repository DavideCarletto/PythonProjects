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



if __name__ == "__main__":
    st.title("🏋 :orange[Corsi]")

    if check_connection():
       visualize_metric_courses()

