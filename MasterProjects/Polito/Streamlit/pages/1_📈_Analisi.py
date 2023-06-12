import collections

import streamlit as st
from utils.utils import *
import pandas as pd

def create_tab_prodotti(tab_prodotti):
    col1, col2, col3 = tab_prodotti.columns(3)
    payment_info = execute_query(st.session_state["connection"], "SELECT SUM(amount) AS 'Total Amount', MAX(amount) AS 'Max Payement', AVG(amount) AS 'Average Payement' FROM payments")
    payment_info_struct = [dict(zip(payment_info.keys(), result)) for result in payment_info]
    col1.metric("Importo Totale", f"${compact_form(payment_info_struct[0]['Total Amount'])}")
    col2.metric("Pagamento Massimo", f"${compact_form(payment_info_struct[0]['Max Payement'])}")
    col2.metric("Pagamento Medio", f"${compact_form(payment_info_struct[0]['Average Payement'])}")

    with tab_prodotti.expander("Panoramica Prodotti", True):
        prod_col1,prod_col2,prod_col3 = st.columns([3,3,6])

        sort_param = prod_col1.radio("Ordina per:", ["code", "name", "quantity", "price"])
        sort_choice = prod_col2.selectbox("Odrine:", ["Crescente", "Decrescente"])

        sort_dict = {"Crescente":"ASC", "Decrescente":"DESC"}

        query_base = "SELECT productCode AS code, productName AS name, quantityInStock AS quantity, buyPrice FROM products "
        query_sort = f"ORDER BY {sort_param}{sort_dict[sort_choice]}"

        if prod_col1.button("Mostra", type = "primary"):
            prodotti = execute_query(st.session_state["connection"], query_base+query_sort)
            df_prodotti = pd.DataFrame(prodotti)
            st.dataframe(df_prodotti, use_container_width= True)

    with tab_prodotti.expander("Pagamenti",True):
        query = "SELECT MIN(paymentDate), MAX (paymentDate) FROM payments"
        date = execute_query(st.session_state["connection"], query)
        min_max = [dict(zip(date.keys(), result))for result in date]
        min_value = min_max[0]["MIN(paymentDate)"]
        max_value = min_max[0]["MAX(paymentDate)"]

        date_range = st.date_input("Seleziona l'intervallo", value =(min_value, max_value))


        query = f"SELECT paymentDate, SUM(amount) AS 'Total'Amount FROM payments WHERE paymentsDate {date_range[0]} > AND paymentsDate < {date_range[1]}"
        paymentsDate = execute_query(st.session_state("connection", query))
        df_paymentDate = pd.DataFrame(paymentsDate)

        if df_paymentDate.empty:
            st.warning("Nessun dato trovato", icon = "⚠")
        else:
            df_paymentDate["Total Amount"] = df_paymentDate["Total Amount"]
            df_paymentDate["paymentDate"] = df_paymentDate["paymentDate"]
            st.line_chart(df_paymentDate, x = "paymentDate", y = "Total Amount")

def create_tab_staff(tab_staff):
    president_query = "SELECT lastName, firstName from employes WHERE jobTitle= 'President'"
    president = execute_query(st.session_state["conncecion"], president_query)

    vp_sales_query = "SELECT lastName, firstName from employes WHERE jobTitle= 'VP Sales'"
    vp_sales = execute_query(st.session_state["connection"], vp_sales_query).mapping().first

    col1, col2, col3 = tab_staff.columns(3)
    col1.markdown(f"### :blue[PRESIDENT:] {president['firstName']} {president['lastName']}")
    col3.markdown(f"### :orange[VP SALES:] {vp_sales['firstName']} {vp_sales['lastName']}")

    # MANCA LA PARTE SULLO STAFF"

def create_tab_clienti(tab_clienti):
    col1, col2 = tab_clienti.columns(2)

    query = "SELECT COUNT (*) AS 'numeroClienti', country FROM customers GROUP by country order by 'numeroClienti' DESC;"
    result = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(result)
    col1.subheader("Distribuzione")
    col1.dataFrame(df, use_container_width=True)

    query = "manca la query"
    result = execute_query(st.session_state["connection"], query)
    df = pd.DataFrame(result)
    col2.subheader("Clienti USA")
    col2.dataFrame(df, use_container_width=True)


#ogni tab ha una funzione separata

if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti,tab_staff,tab_clienti=st.tabs(["Prodotti","Staff","Clienti"])

    if check_connection():
        create_tab_prodotti(tab_prodotti)
        create_tab_staff(tab_staff)
        create_tab_clienti(tab_clienti)