import pandas as pd
import streamlit as st
from utils.utils import  *
from pandas.api.types import CategoricalDtype
import altair as alt
from operator import itemgetter

def visualize_graph():
    st.markdown("#### Di eseguito i :red[grafici] riguardanti le lezioni programmate")
    st.markdown("##### Numero di lezioni per orario:")
    query = "SELECT SUBSTRING_INDEX(OraInizio, ':', 1) AS Ora, COUNT(*) AS Numero_Lezioni FROM PROGRAMMA GROUP BY Ora ASC"
    date = execute_query(st.session_state["connection"], query)
    df_lezioni = pd.DataFrame(date)
    st.bar_chart(df_lezioni, x = "Ora", y = "Numero_Lezioni")

    st.markdown("##### Numero di lezioni per giorno:")
    query = "SELECT COUNT(*) AS 'Num_Lezioni', Giorno FROM programma GROUP BY Giorno"
    lessons_per_day = execute_query(st.session_state["connection"],query)
    lessons_per_day_list = [dict(zip(lessons_per_day.keys(), result)) for result in lessons_per_day]
    # print(lessons_per_day_list)
    lessons_per_day_list[0]["order"] = 3
    lessons_per_day_list[1]["order"] = 0
    lessons_per_day_list[2]["order"] = 1
    lessons_per_day_list[3]["order"] = 2
    lessons_per_day_list[4]["order"] = 4
    lessons_per_day_list = sorted(lessons_per_day_list, key=itemgetter("order"))
    # print(lessons_per_day_list)
    lessons_list = []
    for row in lessons_per_day_list:
        lessons_list.append((row["Giorno"], row["Num_Lezioni"]))
    df_daily_lessons = pd.DataFrame(lessons_list, columns=["Giorno", "Num_Lezioni"])
    df_daily_lessons["Giorno"] = df_daily_lessons["Giorno"].astype(str)
    # print(df_daily_lessons)
    st.altair_chart(alt.Chart(df_daily_lessons).mark_line().encode(x=alt.X("Giorno", sort=None), y=alt.Y("Num_Lezioni")),use_container_width=True)

if __name__ == "__main__":
    st.title("📊️ Lezioni")

    if check_connection():
        visualize_graph()