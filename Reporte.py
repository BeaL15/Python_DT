import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


df = pd.read_csv("Data limpia.csv", na_values=['='])

profile = ProfileReport(df, title="Importacion Chocolates", dataset={
        "description": "Este es mi primer reporte con Streamlit",
        "copyright_holder": "Análisis por Beatriz P.S",
        "copyright_year": "2022"},
    variables={
        "descriptions": {
           "Partida aduanera" : "Partida aduanera"
        }
    }
)


st.title("Reporte de Imp Chocolates")
st.write(df)
st_profile_report(profile)
