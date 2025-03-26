
import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
df = pd.read_csv("dados.csv")

# Título e logo
st.image("logo-clara.png", width=150)
st.markdown("<h1 style='text-align: center;'>Gestão de Tráfego</h1>", unsafe_allow_html=True)
st.markdown("## Painel de Resultados - Porto de Areia Santa Eliza")

# Lista de campanhas
campanhas = df["nome_campanha"].unique()
campanha_selecionada = st.selectbox("Selecione a campanha", campanhas)

# Filtrar dados da campanha
filtro = df[df["nome_campanha"] == campanha_selecionada]

# Cálculos
gasto = filtro["gasto"].values[0]
leads = filtro["leads"].values[0]
try:
    custo_por_resultado = gasto / float(leads) if leads else 0
except:
    custo_por_resultado = 0

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Gasto", f"R$ {gasto:,.2f}")
col2.metric("Leads", f"{leads:,.1f}")
col3.metric("Custo por Lead", f"R$ {custo_por_resultado:,.2f}")

# Tabela de referência
st.markdown("### 📋 Tabela de Campanhas")
st.dataframe(df[["nome_campanha", "gasto", "leads"]])

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center;'>Desenvolvido por Enrico Tráfego Profissional.</div>", unsafe_allow_html=True)
