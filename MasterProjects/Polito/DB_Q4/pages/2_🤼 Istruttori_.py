import pandas as pd
import streamlit as st
from utils.utils import *
from datetime import date


def visualize_tab_istruttori(query):
    # print(query)
    date = execute_query(st.session_state["connection"], query)
    df_istruttori = pd.DataFrame(date)
    # st.dataframe(df_istruttori, use_container_width= True)

    if df_istruttori.empty:
        st.markdown("##### Non ci sono istruttori disponibili che rispettano i criteri di ricerca")

    else:
        st.markdown("##### :green[Elenco] istruttori:")
        for index, row in df_istruttori.iterrows():
            st.text(f"Nome: {row['Nome']}")
            st.text(f"Cognome: {row['Cognome']}")
            st.text(f"Codice Fiscale: {row['CodFisc']}")
            st.text(f"Data di nascita: {row['DataNascita']}")
            st.text(f"Email: {row['Email']}")
            st.text(f"Telefono: {row['Telefono']}")
            st.text("---------------------------------------------")

if __name__ == "__main__":
    st.title("🤼 :red[Istruttori]")

    if check_connection():

        filter = st.text_input(label="Filtra per cognome")
        date_min = date(1970, 1, 1)
        date_max = date(2023, 12, 31)

        # Crea il campo di input per l'intervallo di date

        query = "SELECT * FROM ISTRUTTORE"
        date_selezionate = st.date_input('Seleziona un intervallo di date', (date_min, date_max))

        if len(date_selezionate) == 2:
            if filter != "":
                query = query + f" WHERE Cognome = '{filter}' AND DataNascita BETWEEN '{date_selezionate[0]}' and '{date_selezionate[1]}'"

            else:
                query = query + f" WHERE DataNascita BETWEEN '{date_selezionate[0]}' and '{date_selezionate[1]}'"

            visualize_tab_istruttori(query)

