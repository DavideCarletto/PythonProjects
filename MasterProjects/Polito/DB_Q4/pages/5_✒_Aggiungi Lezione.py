import pandas as pd
import streamlit as st
from utils.utils import  *

def check_info(lezioni_dict):
    for value in lezioni_dict.values():
        if value=='':
            return False
    return True

def check_no_lezioni_giorno(values):
    cod_c = values[5]
    giorno = values[1]

    query = f"SELECT DISTINCT GIORNO FROM PROGRAMMA WHERE CODC = '{cod_c}'"
    date = execute_query(st.session_state["connection"], query)

    giorni_corso = [row[0] for row in date]

    if giorno not in giorni_corso:
        return True

    return False

def insert(lezioni_dict):
    if check_info(lezioni_dict):
        attributi=", ".join(lezioni_dict.keys())
        valori=tuple(lezioni_dict.values())

        if check_no_lezioni_giorno(valori):
            query=f"INSERT INTO programma ({attributi}) VALUES {valori};"
            #try-except per verificare che l'operazione MySQL abbia avuto successo, generare un errore altrimenti
            try:
                execute_query(st.session_state["connection"],query)
                st.session_state["connection"].commit()
            except Exception as e:
                st.error(e)
                return False
            return True
        else:
            return False

def get_istruttori():
    query = "SELECT CodFisc from istruttore"
    date = execute_query(st.session_state["connection"], query)
    istruttori_list = [row[0] for row in date]
    # print(istruttori_list)
    return istruttori_list

def get_corsi_list():
    query = "SELECT CodC from corsi"
    date = execute_query(st.session_state["connection"], query)
    corsi_list = [row[0] for row in date]
    return corsi_list

if __name__ == "__main__":
    st.title("🖊 Aggiungi :green[lezione settimanale]")

    if check_connection():
        with st.form("my_form"):

            st.write("Aggiungi una lezione al DB")
            istruttori_list  = get_istruttori()
            cod_fisc = st.selectbox("Selezionare l'istruttore che detiene la lezione", istruttori_list)

            corsi_list = get_corsi_list()
            cod_corso = st.selectbox("Selezionare il corso su cui si basa la lezione", corsi_list)

            days_list = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"]
            day = st.selectbox("Selezionare il giorno della lezione", days_list)

            ora_inizio = st.time_input("Orario di inizio")
            ora_inizio_str = ora_inizio.strftime("%H:%M:%S")
            # print(ora_inizio_str)

            durata = st.slider("Durata della lezione (minuti)", min_value=30, max_value=60)

            sala = st.slider("Inserire il numero della sala", min_value=1, max_value=10)
            sala = "S"+str(sala)
            # print(sala)

            submitted = st.form_submit_button("Aggiungi")
            insert_dict = {"CodFisc": cod_fisc, "Giorno":day, "OraInizio":ora_inizio_str, "Durata":durata, "Sala":sala, "CodC":cod_corso}

        if submitted:
            #verificare che l'inserimento sia andato a buon fine oppure no
            if insert(insert_dict):
                st.success("Hai inserito questa lezione: ",icon='✅')
                st.write(insert_dict)
            else:
                st.error("Impossibile aggiungere la lezione.",icon='⚠️')