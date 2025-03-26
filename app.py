
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

df = pd.read_csv("dados.csv")

campanhas = df["nome_campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)
filtro = df[df["nome_campanha"] == campanha_selecionada]

gasto = filtro["gasto"].values[0]
leads = filtro["leads"].values[0]

col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.1f}")

# Calcular Custo por Lead
try:
    leads = float(leads)
    custo_por_resultado = gasto / leads if leads > 0 else 0
    col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")
except:
    col3.metric("Custo por Lead", "Erro")
