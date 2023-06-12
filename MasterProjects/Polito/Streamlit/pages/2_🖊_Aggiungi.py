import streamlit as st
from utils.utils import *

def create_form():
    with st.form("Nuovo Prodotto"):
        st.header(":blue[Aggiungi prodotto:]")

        categorie, scale, venditori = get_info()

        code = st.text_input("Codice prodotto", placeholder="S**_****")
        nome = st.text_input("Nome prodotto", placeholder="Inserisci il nome del prodotto")
        categoria = st.selectbox("Categoria", categorie)
        scala = st.selectbox("Scala prodotto", scale)
        venditore = st.selectbox("Venditore",venditori)

        descrizione = st.text_area("Descrizione", placeholder="Descrivimi:")

        qta = st.slider("Quantità", 0, 100000)
        prezzo = st.number_input("Prezzo",3, 0, step=2.5)
        msrp = st.number_input("MSRP")

        insert_dict = {"productCode":code, "productName": nome, "productLine":categoria, "productScale":scala, "productVendor":venditore, "productDesc": descrizione, "productQta":qta,
                       "productPrice":prezzo, "productMSRP":msrp}
        submitted = st.form.submit_button("Aggiungi")

        if submitted:
            if insert(insert_dict):
                print("Fatto")



def check_info(product_dict):
    for value in product_dict.values():
        if value == '':
            return False

def insert(prod_dict):
    if check_info(prod_dict):
        attributi = ", ".join(prod_dict.keys())
        valori = tuple(prod_dict.values())
        query = f"INSERT INTO products ({attributi} VALUES {valori})"

        try:
            execute_query(st.session_state["connection"], query)
        except:
            print("non funzia")

def get_list(attributo):
    query = f"SELECT DISTINCT {attributo} FROM products"
    result = execute_query(st.session_state["connection"], query)
    result_list = []

    for row in result.mapping():
        result_list.append(row[attributo])
    return result_list

def get_info():
    return get_list("productLine"), get_list("productScale"), get_list("productVengor")

if __name__ == "__main__":
    st.title("🖊 Aggiungi")
    if check_connection():
        create_form()
