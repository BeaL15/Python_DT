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
           "Descripcion de la Partida Aduanera" : "Descripcion de la partida aduanera"
           "Importador" : "Importador"
           "Kg Bruto" : "Kg bruto"
           "Kg Neto" : "Kg neto"
           "U$ FOB Tot" : "U$ Fob"
           "Pais de Origen" : "Pais de Origen"
           "Via" : "Via"
           "Agente de Aduana" : "Agente de aduana"
           "Almacen" : "Almacen"
           "Descripcion Comercial" : "Descripcion"
           "Ad Valorem" : "Ad Valorem"
           "IGV" : "Igv"
           "IPM" : "Ipm"
           "Canal" : "Canal"
           "Año" : "Año"
           "mes_e": "Mes"
        }
    }
)


st.title("Reporte de Imp Chocolates")
st.write(df)
st_profile_report(profile)
