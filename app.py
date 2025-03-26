
import streamlit as st
import pandas as pd

# Carrega os dados
df = pd.read_csv("dados.csv")

st.image("logo-clara.png", width=150)
st.markdown("## Gestão de Tráfego")
st.markdown("### Painel de Resultados - Porto de Areia Santa Eliza")

# Filtro de campanha
campanhas = df["campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

filtro = df[df["campanha"] == campanha_selecionada]

# Cálculos
gasto = filtro["gasto"].values[0]
leads = filtro["leads"].values[0]

try:
    custo_por_resultado = gasto / leads if leads > 0 else 0
except:
    custo_por_resultado = 0

# Exibição
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.1f}")
col3.metric("Custo por Lead", f"R$ {float(custo_por_resultado):,.2f}")
