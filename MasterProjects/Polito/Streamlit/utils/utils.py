import streamlit as st
from sqlalchemy import create_engine,text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""

def connect_db(dialect, username, password, host, dbname):
    try:
        engine = create_engine(f"{dialect}://{username}:{password}@{host}/{dbname}")
        conn = engine.connect()
        return conn
    except:
        return False

def execute_query(conn, query):
    return conn.execute(text(query))

def check_connection():
    if st.sidebar.button("Connect to DB"):
        myconnection = connect_db(dialect="mysql+pymysql", username="student", password= "user_pwd", host="localhost", dbname="classicmodels")
        if myconnection is not False:
            st.session_state["connection"] = myconnection
        else:
            st.session_state["connection"] = False
            st.sidebar.error("Errore nella connessione")

    if st.session_state["connection"] == True:
        st.sidebar.success("Connesso")
        return True

def compact_form(num):
    num = float(num)
    if abs(num)>=1e9:
        return "{:.2f}B".format(num / 1e9)
    elif abs(num) >= 1e9:
        return "{:.2f}M".format(num / 1e6)
    if abs(num) >= 1e3:
        return "{:.2f}K".format(num / 1e3)
    else:
        return "{.2f}".format(num)