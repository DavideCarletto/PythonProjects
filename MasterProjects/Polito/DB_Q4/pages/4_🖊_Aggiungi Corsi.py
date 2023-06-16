import pandas as pd
import streamlit as st
from utils.utils import  *

def check_info(corsi_dict):
    for value in corsi_dict.values():
        if value=='':
            return False
    return True

def insert(corsi_dict):
    if check_info(corsi_dict):
        attributi=", ".join(corsi_dict.keys())
        valori=tuple(corsi_dict.values())
        query=f"INSERT INTO corsi ({attributi}) VALUES {valori};"
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

if __name__ == "__main__":
    st.title("🖊 Aggiungi :green[corsi]")

    if check_connection():
        with st.form("my_form"):
            st.write("Aggiungi un nuovo corso al DB")
            codc = st.text_input("Codice corso")
            name = st.text_input("Nome corso")
            type = st.text_input("Tipo di corso")
            lvl = st.slider("Livello del corso", 1,4)
            # Every form must have a submit button.
            submitted = st.form_submit_button("Aggiungi")

            insert_dict = {"CodC": codc, "Nome":name, "Tipo":type, "Livello":lvl}


        if submitted:
            #verificare che l'inserimento sia andato a buon fine oppure no
            if insert(insert_dict):
                st.success("Hai inserito questo corso: ",icon='✅')
                st.write(insert_dict)
            else:
                st.error("Impossibile aggiungere il corso.",icon='⚠️')